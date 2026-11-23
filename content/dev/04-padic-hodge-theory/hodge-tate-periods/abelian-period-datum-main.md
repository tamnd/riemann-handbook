---
id: abelian-period-datum-main
title: From an abelian scheme over A_inf modulo xi squared to a Hodge-Tate period datum
kind: theorem
decl: GlobalTheory.AbelianPeriodDatum.main
module: Development.AbelianVarietyTheory.Proofs.UnramifiedDepth.ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBu
covers: 345
status: drafted
drafted_by: writer@claude
---
This theorem starts from an abelian scheme with a symmetric line bundle on $G \times G$ and an action of a ring with involution. It builds a functor of points with a biextension, and a Hodge-Tate datum on a $p$-adic tower that matches the ring action. The code uses it under the name [exists-period-tower-datum-of-abelian-scheme-symmetric-bundle](/entry/exists-period-tower-datum-of-abelian-scheme-symmetric-bundle/), below the [literature step](/step/every-character-of-literature/).

## Statement

Let $p$ be a prime, $C$ an algebraically closed field of characteristic $0$ with a valuation, and $O$ its ring of integers, $p$-adically complete. Let $\varepsilon \in O^\flat$ be such that $(\varepsilon^{1/p})^\sharp$ is a primitive $p$-th root of unity. Put $A_{\inf} = W(O^\flat)$, $\xi = \sum_{i<p} [\varepsilon^{1/p}]^i$ and $R_0 = A_{\inf}/\xi^2$. Assume:

1. $G$ is a commutative abelian scheme over $R_0$, smooth of relative dimension $g$, and $[p]$ is finite, flat and surjective.
2. $P$ is a line bundle on $G \times G$. Its theta bundle has a generator, $P$ is trivial on $1 \times G$ and on $G \times 1$, and $P \cong \mathrm{swap}^* P$.
3. For a $C$-point $x$, if $P$ is trivial on $G \times x$, then $x = 1$. Also $\#G(C)[p] = p^{2g}$.
4. $G'$ is an abelian scheme over $O$ with a group map $\varphi : G' \to G$ that is a pullback square.
5. A ring $O_0$ with an involution $c$ acts on $G'$. For each $a$, the bundle $(a \times 1)^*P \otimes ((1 \times c(a))^*P)^{-1}$ has a generator. This is a Rosati condition.

Then:

1. There is a biextension datum $B$ (`BX`) over local $R_0$-algebras, with a bijective, additive and natural map $e_R : B(R) \to G(R)$.
2. There is an action $\mathrm{Ad}$ of $O_0$ on $B$ that matches the action on $G'$ through $\varphi$ and $e$.
3. There are a dual tower and a datum $D$ (`Dat`) on the tower $R_n = O/p^{n+1}$, $R'_n = R_0/p^{n+1}$. Its Hodge-Tate part has projectors $P = 0$ and $P_L = 0$.
4. $\mathrm{Ad}(a)$ acts on tangent vectors by the matrix $\rho_L(1 \otimes a)$ of $D$.
5. $\mathrm{Ad}(a)$ acts on the chosen $p^{n+1}$-torsion points $\tau_j(n)$ by $\tau_j(n) \mapsto \sum_k \rho(1 \otimes a)_{kj}\, \tau_k(n) \bmod p^{n+1}$.

## Proof

The proof chains proved lemmas.

1. `ainf_thetaQuotRing_isLocalRing` shows that $R_0$ is local.
2. `nonempty_isBiext_of_cube_gen` makes $P$ a biextension $\beta$. `BiextSym.main` makes it symmetric.
3. `BXOf.main` builds $B$ and $e$ from $\beta$.
4. `exists_oAdj_of_rosatiAdjoint` turns the Rosati condition into $\mathrm{Ad}$. The local lemma `ring_laws` shows that $\mathrm{Ad}$ respects $1$, sums and products, and is adjoint for $c$.
5. The local lemma `divisible_and_card` shows that $B(O)$ is $p$-divisible and has as many $p$-torsion points as $G(C)$. So it has $p^{2g}$ of them.
6. `pairing_nondegenerate_integral_torsion` gives a nondegenerate pairing on torsion. It uses hypothesis 3.
7. `GlobalTheory.PeriodDatum.main` assembles the tower and $D$.

We read the statements of these lemmas, not their proofs.

## In the Lean code

The theorem is in [ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBu.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsPeriodTowerDatumOfAbelianSchemeSymmetricBu.lean#L132). The last step is [ExistsCompatibleBasis.lean](lean:Development/AbelianVarietyTheory/Proofs/UnramifiedDepth/ExistsCompatibleBasis.lean#L82). The structures are `BX` in [SqZeroOfSpan.lean](lean:ReciprocityTheory/DualLattices/SqZeroOfSpan.lean#L56), `Dat` in [TowerZeroSurjective.lean](lean:ReciprocityTheory/DualLattices/TowerZeroSurjective.lean#L13), and `HodgeTateData` in [FormalChartAtZero.lean](lean:ReciprocityTheory/DualLattices/FormalChartAtZero.lean#L162). The ring $R_0$ is in [AinfTower.lean](lean:ReciprocityTheory/DualLattices/AinfTower.lean#L16).

Every hypothesis is used in the proof. The conclusion fixes the two projectors to $0$, so the conditions on the projector fields of `HodgeTateData` hold trivially here.
