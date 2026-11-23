---
id: prismatic-dieudonne-hodge
title: A Dieudonné theory over A_inf with its Hodge filtration
kind: theorem
decl: UpperTheory.Lit.prismaticDieudonneHodge
module: Development.AutomorphicArithmetic.ThetaCorrespondence.PrismaticDieudonne.PrismaticDieudonneHodge
covers: 1708
status: drafted
drafted_by: writer@claude
---
This theorem gives, for $p$-divisible groups over the ring of integers of an algebraically closed field, a functor to finite free modules over Fontaine's ring $A_{\inf}$ with a Frobenius and a Hodge filtration. Its two users: the leaf `prismatic_dieudonne_hodge_of_literature` puts it in the field `q4` of the bundle [PublishedHodgeBundleTheorems](/step/published-results-arithmetic/), and `farguesExact` of the same file turns it into `FarguesExact`, an input of the volume branch of [EveryCharacter from the literature and VWin](/step/every-character-of-literature/). Most of its weight is in [`window_matrices`](/entry/window-matrices/) (1,206 of 1,708 declarations).

## Statement

Let $p$ be a prime and $C$ an algebraically closed field of characteristic $0$ with a valuation $v$. Let $\mathcal{O}$ be the ring of integers of $v$; suppose that $p$ is not a unit in $\mathcal{O}$ and that $\mathcal{O}$ is $p$-adically complete. Let $A_{\inf} = W(\mathcal{O}^\flat)$ with Frobenius $\varphi$ and Fontaine's map $\theta \colon A_{\inf} \to \mathcal{O}$ (see [[Fontaine's period rings|K6HW8YWCQJ]]). Let $\varepsilon \in \mathcal{O}^\flat$ be such that its first root, untilted, is a primitive $p$-th root of unity. Let $\xi \in A_{\inf}$ be the element `xi ε` (not unfolded).

**Theorem.** There are contravariant functors $M$ to $A_{\inf}$-modules and $D$ to $\mathcal{O}$-modules on the category of $p$-divisible groups $G$ over $\mathcal{O}$, with natural maps $\varphi_G \colon M(G) \to M(G)$ ($\varphi$-semilinear), $r_G \colon M(G) \to D(G)$ ($\theta$-semilinear), $\iota_G \colon \omega_G \to D(G)$ and $\pi_G \colon D(G) \to \operatorname{Lie}(G^\vee)$, such that:

1. $M$ is additive, and $M(G)$ is free of rank equal to the height of $G$;
2. $\varphi(\xi) M(G) \subseteq \varphi_G(M(G))$;
3. $r_G$ is onto with kernel $\xi M(G)$, so $D(G) = M(G) \otimes_{\theta} \mathcal{O}$;
4. $0 \to \omega_G \to D(G) \to \operatorname{Lie}(G^\vee) \to 0$ is exact (the Hodge filtration);
5. $M(\mathbb{Q}_p/\mathbb{Z}_p) \cong A_{\inf}$ with $\varphi_G = \varphi$, and $M(\mu_{p^\infty}) \cong A_{\inf}$ with $\varphi_G = \varphi(\xi)\,\varphi$;
6. each $A_{\inf}$-linear map $M(\mu_{p^\infty}) \to M(\mathbb{Q}_p/\mathbb{Z}_p)$ that commutes with the Frobenius maps is $M(f)$ for exactly one $f \colon \mathbb{Q}_p/\mathbb{Z}_p \to \mu_{p^\infty}$.

Here $\mathbb{Q}_p/\mathbb{Z}_p$ and $\mu_{p^\infty}$ stand for `const p O` and `PDivGroup.mu p O`, by their names. By its name and shape, the theorem is a form of the prismatic Dieudonné theory of Anschütz and Le Bras (Forum Math. Pi 11, 2023) over $\mathcal{O}_C$. We have not checked each clause against that paper.

## Proof

The hypothesis on $\varepsilon$ gives that the $n$-th root of $\varepsilon$, untilted, is a primitive $p^n$-th root of unity for each $n$ (`isPrimitiveRoot_untilt_root`). Then:

1. `exists_bFrame` gives a frame `BFrame ε`.
2. For $G$ connected with connected dual, [`window_matrices`](/entry/window-matrices/) gives matrices over the frame ring, with bases of $T_pG$, $\omega_G$ and $\operatorname{Lie}(G^\vee)$ and a family in $T_pG^\vee$, that satisfy Frobenius relations.
3. `window_lift_to_fontaineAinf_matrices` lifts these matrices to $A_{\inf}$.
4. `hasDatum_of_matrices` turns the lifted matrices into a datum `HasDatum` for $G$. `hasDatum_biconn_of` puts steps 1 to 4 together.
5. `pDivisibleGroup_datum_of_connected_dual_connected` extends the datum from such $G$ to all $p$-divisible groups.
6. `prismaticDieudonneHodge_of_hodgeTateDatum` builds $M$, $D$ and the maps from the data.

We have not unfolded `HasDatum` or `BFrame`.

## In the Lean code

The theorem is at [PrismaticDieudonneHodge.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean#L19). The statement is at [InjectiveOfSmulMemRange.lean](lean:Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/InjectiveOfSmulMemRange.lean#L62).

- Clause 6 is full faithfulness for one pair of objects only. The statement does not say that $M$ is fully faithful or an equivalence.
- The valuation $v$ has values in $\mathbb{R}_{\geq 0}$, and $C$ need not be complete; only $\mathcal{O}$ is assumed $p$-adically complete.
- A different statement with the same short name, `GlobalTheory.PrismHodge.PrismaticDieudonneHodgeAt`, is in [HodgeAtOfPrismaticDieudonneAt.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HodgeAtOfPrismaticDieudonneAt.lean#L62). It has other fields (`lie`, `dR`). This theorem uses the one of the namespace `GlobalTheory.Published`.
