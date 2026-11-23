---
id: leibniz-ord
title: The Leibniz rule for derivatives, with the order of the layers
kind: theorem
decl: GlobalTheory.RgGu.Leib.Hand.leibnizOrd
module: Development.WeilBound.RepresentationTheoryGL.GenericUnitaryGL.ComplementarySeries.HighestDerivativeProducts.HighestDerivProd
covers: 1582
status: drafted
drafted_by: writer@claude
---
This theorem is the Leibniz rule for the Bernstein-Zelevinsky derivatives of a product of two representations of general linear groups over a $p$-adic field. Its callers `bern` and `bernAt` use it to prove `BernAt`, below [EveryCharacter from the Galois row](/step/every-character/).

## Statement

Let $k$ be a nonarchimedean local field. Let $\psi$ be a nontrivial unitary character of $k$. For a complex representation $\pi$ of $\mathrm{GL}_{n+j}(k)$, let $\pi^{(j)}$ be its $j$-th derivative, a representation of $\mathrm{GL}_n(k)$. In the Lean code (`derivB`), $\pi^{(0)} = \pi$ and $\pi^{(j+1)} = \Psi^-(\Phi^-)^{j}(\pi|_{P})$. Here $P$ is the mirabolic subgroup (last row $(0, \dots, 0, 1)$), and $\Phi^-$, $\Psi^-$ are the Jacquet functors along the last column for $\psi$ and for the trivial character. Let $\nu^s = |\det|^s$. Let $\pi_1 \times \pi_2$ be normalized parabolic induction from the block upper triangular parabolic subgroup (`prod2`).

**Theorem.** Let $r, t, \ell, n \ge 0$ with $r + t = n + \ell$. Let $\pi_1$ and $\pi_2$ be smooth representations of $\mathrm{GL}_r(k)$ and $\mathrm{GL}_t(k)$. Then $D = (\pi_1 \times \pi_2)^{(\ell)}$ has a decreasing chain of subrepresentations
$$D = F_0 \supseteq F_1 \supseteq \dots \supseteq F_{\ell+1} = 0$$
such that, for $0 \le i \le \ell$:

- if $i \le r$ and $\ell - i \le t$, then $F_i / F_{i+1} \cong \pi_1^{(i)} \nu^{(\ell - i)/2} \times \pi_2^{(\ell - i)} \nu^{i/2}$;
- otherwise $F_i = F_{i+1}$.

With their normalization of derivatives, the twists go away. This is the Leibniz rule (Bernstein and Zelevinsky, Ann. Sci. ENS 10 (1977), Section 4), with the order of the layers made explicit.

## Proof

The proof applies `leibniz_order_of_exact_sequences` to six facts. Let $\tau$ be a representation of a mirabolic group and $\rho$, $\sigma$ of general linear groups. The products $\tau \times \sigma$ and $\rho \times \tau$ are `prodPGn` and `prodGPn`. The normalized functors $\Phi = \nu^{-1/2}\Phi^-$ and $\Psi = \nu^{-1/2}\Psi^-$ are `phiN` and `psiN`. The six facts are:

1. `ResSeq` (`residue_sequence_holds`): $(\pi_1 \times \pi_2)|_P$ has a subrepresentation isomorphic to $\pi_1|_P \times \pi_2$, with quotient $\pi_1 \times \pi_2|_P$.
2. `PsiGP` (`psi_gp_commutation_holds`): $\Psi(\rho \times \tau) \cong \rho \times \Psi\tau$.
3. `PhiGP` (`phi_gp_commutation_holds`): $\Phi(\rho \times \tau) \cong \rho \times \Phi\tau$.
4. `PsiPG` (`psiPG`): $\Psi(\tau \times \sigma) \cong \Psi\tau \times \sigma$.
5. `PhiPG` (`phiPG`): $\Phi(\tau \times \sigma)$ has a subrepresentation isomorphic to $\Phi\tau \times \sigma$, with quotient $\Psi\tau \times \sigma|_P$.
6. `PhiPG0` (`phi_pg_rank_zero_holds`): if $\tau$ is a representation of the mirabolic group of rank 0, then $\Phi(\tau \times \sigma) \cong \Psi\tau \times \sigma|_P$.

The general theorem `leibnizOrd_of_parts` works with the normalized derivative $d_\ell = \Psi \Phi^{\ell - 1}(\,\cdot\,|_P)$ (`dG`). In `main_chain`, fact 1 splits $(\pi_1 \times \pi_2)|_P$ and the exact functor $\Psi\Phi^{\ell-1}$ is applied. On the quotient, facts 2 and 3 give $d_\ell$ of it as $\pi_1 \times d_\ell \pi_2$, or zero when $\ell > t$ (`gp_iso`, `gp_zero`). On the subrepresentation, `pg_chain` runs an induction on $\ell$ with facts 4, 5 and 6: each $\Phi$ splits off one more layer. Then `derivative_twisted_iso` gives $\pi^{(j)} \cong (d_j \pi) \nu^{j/2}$. Then `exists_antitone_filtration_of_chain` gives $F$. The rest is bookkeeping.

## In the Lean code

The theorem is in [HighestDerivProd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/ComplementarySeries/HighestDerivativeProducts/HighestDerivProd.lean#L23). It only passes the six facts along to `leibnizOrd_of_parts` in [LeibnizOrderOfExactSequences.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/LeibnizOrderOfExactSequences.lean#L318). `LeibnizOrd` and the facts are defined in [LeibnizOrd.lean](lean:Development/WeilBound/RepresentationTheoryGL/GenericUnitaryGL/LeibnizOrders/LeibnizOrd.lean#L36). We have not read the proofs of the six facts.

The file name says "highest derivative of a product", but the theorem is the full Leibniz rule. `HighestDerivProd` is a different definition, about the top derivative $(\pi_1 \times \pi_2)^{(r+t)}$. The file imports about ten modules whose declarations the proof does not name. We read `dpow n s` as $|\det|^s$ from its name, without unfolding `absPow`.
