---
id: sum-hv-primary-kernel
title: A sum of harmonic values over the primary part of a kernel
kind: theorem
decl: GlobalTheory.sum_hv_primary_kernel
module: Development.AbelianVarietyTheory.Proofs.RingsOfIntegers.SumHvPrimaryKernel
covers: 574
status: drafted
drafted_by: writer@claude
---
This theorem bounds a sum of harmonic values of translated sections over the $\ell$-primary part of the kernel of a similitude $pq$. The sum is $\#(\ker q) \cdot \prod_\tau \tau(\det p)^{m_\tau}$ times an element of valuation at least $-\rho$. It reduces the sum to the formal group, where [`sum_hv_formal_kernel`](/entry/sum-hv-formal-kernel/) does the work. The [statement form](/entry/sum-hv-primary-kernel-alt/) restates it for its users below the [literature layer](/step/every-character-of-literature/).

## Statement

Let $X_o$ be a moduli scheme over a CM field $E$, with abelian scheme $A$, line bundle $L$ and coefficient datum $c$, and let the star operation on $\mathcal{O}_E$ be the conjugation of the datum. Let $T$ be a complete [[discrete valuation ring|MGM3CNJW9V]] of characteristic $0$ with valuation $v$, $\iota \colon c.F \to \operatorname{Frac} T$, $y$ an integral framed point with point $x$, and $C$ an integral chart at $y$ with `Good3` (not unfolded here). Let $\nabla$ agree with the charts (`IsNab`), and let `ChBound C e ρ w n` hold with $e > 0$. For sections $F_b$ of $L^k$ and a polynomial $P$, the harmonic value is $\mathrm{hv}(F, P) = \sum_m P_m \prod_b \nabla(y, k, F_b, m_b)$.

Hypotheses:

- $\ell$ is a prime and not a unit in $T$;
- $N$ is odd, $N^2 = kM$ with $\gcd(k, \ell) = 1$, and the $M$-torsion of $A_x$ is rational (`AllRat`);
- $p, q, g$ are $n \times n$ matrices over $\mathcal{O}_E$ with $(pq)^*(pq) = N^2$ and $gq = k_1 N$, $\gcd(k_1, \ell) = 1$;
- $a \colon J \to A_x^n$ is injective, with image the $u$ that $pq$ kills and whose coordinates have $\ell$-power order;
- Weil pairings of level $N^2$ between the $a_i$ have product $1$ (`WeilIs`, not unfolded);
- each $F_b$ is a section of $L^{N^2}$ reached from the frame section (`Reach`), and is fixed by each $\ell$-power point $u$ with $u^N = 1$;
- $G_{i,b}$ is the translate of $F_b$ by $a_{i,b}$ (`Moves`, not unfolded);
- $P \in$ `HH c w n`, and $\iota(s \cdot P')$ is integral (`FFV`), where $P'$ is $P$ after the change of variables by $pq$.

**Theorem.** There is $z \in \operatorname{Frac} T$ with $v(z)/e \geq -\rho$ and
$$\iota(s) \sum_{i \in J} \mathrm{hv}(G_i, P) = \#\{i : q a_i = 0\} \cdot \iota\Bigl(\prod_{\tau} \tau(\det p)^{m_\tau}\Bigr) \cdot z.$$

## Proof

Let $W$ be the image of $a$, $W_0 = W \cap \ker q$, and $W_1$ the elements of $W$ with coordinates in the formal group of $C$ (`FormPt`).

1. **$W_0$ does not change $\mathrm{hv}$.** For $u \in W_0$, $gq = k_1 N$ and $\gcd(k_1, \ell) = 1$ give $u^N = 1$, so $u$ fixes each $F_b$. With the Weil pairing hypothesis and $N$ odd, `rel_of_moves` shows that translation by $u$ changes the translates by scalars with product $1$. Since $\mathrm{hv}$ is multilinear (`hv_linear`), it does not change.
2. **Cosets.** The lemma `sum_cosets` on finite abelian groups writes the sum over $W$ as $\#W_0$ times a sum of coset sums over $W_1$. The set $\{z : v(z)/e \geq -\rho\}$ is closed under sums (`le_nval_sum`).
3. **One coset.** On each coset, apply [`sum_harmonicValues_formalKernel_similitude`](/entry/sum-harmonic-values-formal-kernel-similitude/). `splitKernel_formalGroup_of_rational_torsion`, `kills_formalPoints_iff_mem_coordinateKernel` and `reachedSection_regular_on_integralModel` give its hypotheses. Step 1 gives the condition on $\ker q$.

## In the Lean code

The theorem is in [SumHvPrimaryKernel.lean](lean:Development/AbelianVarietyTheory/Proofs/RingsOfIntegers/SumHvPrimaryKernel.lean#L221), with the helpers `sum_cosets`, `Rel` and `rel_of_moves` in the namespace `GlobalTheory.CoreTrace`. The definitions `hv`, `Reach`, `Moves`, `FormPt` and `ChBound` are in [AdaptStd.lean](lean:Development/AbelianVarietyTheory/Definitions/PlaceAdaptation/AdaptStd.lean#L98). Each hypothesis of the theorem is used.
