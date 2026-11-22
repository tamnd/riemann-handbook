---
id: cong-uwg-of
title: Congruences with a fixed type, generic places and a lacunary weight
kind: theorem
decl: UpperTheory.Gal.Int.Cong.congUWG_of
module: Development.AutomorphicArithmetic.Foundations.GaloisRepresentations.IntegralStructures.CongruenceOddLevel.NotApartOfOverPair
covers: 347
status: drafted
drafted_by: writer@claude
---
This theorem proves the congruence statement `CongUWG TyEll (GenOf D) WtLac` from the step statement `StepSt`, for each nonzero family of integer polynomials $D$. Its user is [`congFinG_of_step`](/entry/cong-fin-g-of-step/), which takes $D$ = `DGen`. The parameters `TyEll`, `GenOf` and `WtLac` are explained in that entry. The theorem adds Hecke operators at the places $z \in Z$ that detect genericity, and so it keeps only generic representations in the approximation. Below it are 347 declarations.

## Statement

Let $E$ be a CM field, $\ell$ a prime, $\iota : \overline{\mathbb{Q}}_\ell \cong \mathbb{C}$, $a \geq 1$, $T$ a finite set of non-split places, $U$ a representation that is automorphic off $T$, and $w_0, v'$ split places above $\ell$ over different places of $E^+$.

**Theorem.** Suppose `StepSt` and `FinU` hold, and $D_a \neq 0$ for each $a$. Then there are levels $K_w$ such that $U$ has level $K_w$ off $w_0, v'$, each $K_w$ is open compact, and $K_w$ is hyperspecial where $U$ has Satake parameters. For finite sets $Z, W$ of such places there are constants $c(w,n) \neq 0$ with this property. For each family $O$ of local Hecke operators with eigenvalues $\theta$ on $U$, the tuple $(\theta, \iota^{-1}(c(w,n)\,\mathrm{Sat}_w(U)^n))$ satisfies `PolyApprox` by the same tuples of representations $U'$ that are automorphic off $T$, have level $K_w$, have the weight of $U$ off $w_0, v'$, are lacunary at one $\tau_0$ over $v'$, satisfy `TyEll` at $w_0$, and are generic for $D$ at each $z \in Z$. If the values of $O$ are rational, the $\theta_j$ lie in a finite extension of $\mathbb{Q}_\ell$.

`PolyApprox` $\theta$ $S$ says: for each $\varepsilon > 0$ there are finitely many $\eta \in S$ and coefficients $c_\eta$ with $\lVert P(\theta) - \sum c_\eta P(\eta) \rVert \leq \varepsilon$ for each integer polynomial $P$.

`StepSt` says: for a level $K$ away from $w_0$, an open $K_v$ at $v'$, a weight $\lambda$, and integral Hecke operators $t$ supported away from $w_0, v'$ with eigenvalues $\eta$, the tuple $\eta(U)$ is approximated by tuples $\eta(U')$, where $U'$ has a weight $\mu$ equal to $\lambda$ except over $v'$, lacunary at $\tau_0$, and `TyEll` at $w_0$.

## Proof

1. **Levels.** `exists_level` gives $K$, $K_w$ and $K_v$. `exists_algebraicWeight_definiteUnitaryAutRep` gives the weight $\lambda$ of $U$. Put $K' = K \cap K_v$.
2. **Operators.** For $(w,n) \in W \times \mathbb{Z}$, `exists_powOp` gives an operator with eigenvalue $\mathrm{Sat}_w(U')^n$, and `exists_scale` multiplies it by $c(w,n) \neq 0$ to make it integral. For $z \in Z$, `exists_testOp` gives an operator whose eigenvalue $e_z(U')$ is nonzero exactly when $U'$ is generic for $D_a$ at $z$. `exists_op` realizes $O$.
3. **Finite extension.** `FinU` applied to the operators of $O$ gives the last clause. This is the only use of `FinU`.
4. **Approximation at weight $\lambda$.** `toPolyX_holds`, with `denseGen_holds` and `frameW_holds`, approximates $\eta(U)$ by $\eta(U_1)$ over $U_1$ of weight $\lambda$, level $K'$, generic at $Z$.
5. **Combination.** Let $Q = \prod_{z \in Z} X_z$. For each $U_1$, $Q(\eta(U_1)) \neq 0$, and `StepSt` approximates $\eta(U_1)$. `combine_holds` gives an approximation of $\eta(U)$ by the $\eta(U')$ of `StepSt` with $Q(\eta(U')) \neq 0$, that is, generic at $Z$. `restrict_holds` drops the $Z$ coordinates.
6. The rest is bookkeeping: each $U'$ has the listed properties.

## In the Lean code

The theorem is in [NotApartOfOverPair.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L111). `StepSt` is at [L35](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/NotApartOfOverPair.lean#L35), and `CongUWG` in [ApartOfNotMem.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/CongruenceOddLevel/ApartOfNotMem.lean#L12). `Combine` is in [StGlob.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SeparatingAlgebras/StGlob.lean#L13), and `ToPolyX` in [BlockBoundAlt.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/SeparatingAlgebras/BlockBoundAlt.lean#L44). We have not unfolded `exists_level`, `exists_testOp` and the proofs of `toPolyX_holds` and `combine_holds`.
