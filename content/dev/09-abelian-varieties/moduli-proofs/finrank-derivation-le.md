---
id: finrank-derivation-le
title: The tangent space of a PEL family is at most the dimension of the symmetric domain
kind: theorem
decl: GlobalTheory.PelTan.finrank_derivation_le
module: Development.AbelianVarietyTheory.Proofs.ModuliProofs.FinrankTangentPELFamilyLeSymmetricDomain
covers: 423
status: drafted
drafted_by: writer@claude
---
This theorem bounds the tangent space at a complex point of the base of a PEL family by $\tfrac{[E:\mathbb{Q}]}{2}\,pq$. It is the proof of [its statement form](/entry/finrank-tangent-pel-family-le-symmetric-domain/). [`exists_thetaFam_isPEL_smooth`](/entry/exists-theta-fam-is-pel-smooth/) uses it for the smooth generic fibre. Its dominator in the written proof is the step [EveryCharacter from the literature and VWin](/step/every-character-of-literature/).

## Statement

Assume inputs 2, 3, 9 and 10 of [`topAmpExists`](/entry/top-amp-exists/). Take $E$, $H$, $D$ of signature $(p, q)$, a symplectic basis $(e_i)$ and generators $a \colon J \to \mathcal{O}_E$ as in [`exists_thetaFam_isPEL_smooth`](/entry/exists-theta-fam-is-pel-smooth/). Take a base $b$ of level $N'^2$ over $o$, an element $\rho \in o$ with $\rho^2 = -d$, and ring maps $o \to R \to \mathbb{C}$ that commute with a map $o \to \mathbb{C}$. Let $t$ be a theta level object over $\operatorname{Spec} R$ and $\tau$ a PEL structure on it (`IsPEL`). Assume that $R$ is of finite type over $o$, and that $t$ is unramified in this sense: if $x \colon \operatorname{Spec} \mathbb{C}[\varepsilon] \to \operatorname{Spec} R$ lies over a constant point of $o$, and some object over $\mathbb{C}[\varepsilon]$ is a pullback of $t$ both along $x$ and along the constant point $x_0$ under $x$, then $x = x_0$.

**Theorem.** $\dim_{\mathbb{C}} \operatorname{Der}_o(R, \mathbb{C}) \le \tfrac{[E:\mathbb{Q}]}{2}\,pq$, where $\mathbb{C}$ is an $R$-module through the given map.

The right side is the complex dimension of a product of $[E^+:\mathbb{Q}]$ copies of the symmetric domain of $\mathrm{U}(p, q)$, each of dimension $pq$ (Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces*, Ch. X, type AIII).

## Proof

1. `T.tangent_injects_symmetric_antilinear_commuting` (inputs 2, 3, 10, and the unramified condition) gives the fibre $t_0$ of $t$ at the complex point, a complex uniformization $\mathbb{C}^g/\Lambda$ of $t_0$ with a positive definite Hermitian matrix $H_m$, and an injective linear map $\kappa \colon \operatorname{Der}_o(R, \mathbb{C}) \to M_g(\mathbb{C})$. Each $\Theta$ in its image is symmetric for $H_m$, that is $H_m(\Theta \bar z, w) = H_m(\Theta \bar w, z)$, and commutes in this antilinear sense with the lift of each endomorphism of $t_0$ that comes from $t$.
2. `FibreAct.exists_fibre_act` takes the $\mathcal{O}_E$-action of $\tau$ to $t$ and to $t_0$, with the determinant condition `DetCond` at $\rho$.
3. `KS.exists_linear_lift_action` lifts the action on $t_0$ to a ring map $F \colon \mathcal{O}_E \to \operatorname{End}(\mathbb{C}^g)$.
4. `T.finrank_eigenspace_of_lieMultiplicity` shows that for each embedding $\sigma \colon \mathcal{O}_E \to \mathbb{C}$ the joint $\sigma$-eigenspace of $F$ has dimension $p$ if $\sigma(\sqrt{-d}) = \rho_0$ and $q$ otherwise, where $\rho_0$ is the image of $\rho$ in $\mathbb{C}$.
5. `T.finrank_symm_antilinear_comm_CM_le` is linear algebra: a space of $H_m$-symmetric matrices that commute with $F$ in the sense above has dimension at most $\tfrac{[E:\mathbb{Q}]}{2}\,pq$. Apply it to the image of $\kappa$. Since $\kappa$ is injective, the bound passes to $\operatorname{Der}_o(R, \mathbb{C})$.

## In the Lean code

The theorem is in [FinrankTangentPELFamilyLeSymmetricDomain.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/FinrankTangentPELFamilyLeSymmetricDomain.lean#L21). The lemmas it calls:

- `T.tangent_injects_symmetric_antilinear_commuting` in [TangentInjectsSymmetricAntilinearCommutingStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/TangentInjectsSymmetricAntilinearCommutingStatement.lean#L14), [entry](/entry/tangent-injects-symmetric-antilinear-commuting/), a second name for [`KS.tangent_injects_symm_antilinear`](/entry/tangent-injects-symm-antilinear/);
- `FibreAct.exists_fibre_act` in [ExistsFibreAct.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/ExistsFibreAct.lean#L58);
- `KS.exists_linear_lift_action` in [EqZeroOfLineSubsetDiscrete.lean](lean:Development/AbelianVarietyTheory/Proofs/ModuliProofs/EqZeroOfLineSubsetDiscrete.lean#L38);
- `T.finrank_eigenspace_of_lieMultiplicity` and `T.finrank_symm_antilinear_comm_CM_le`, statement forms of `UnifEigenRank.finrank_eigenspace_of_lieMult` and `KS.DimPEL.finrank_symm_comm_le`.

`IsSymm` and `Comm` are in [IsSymm.lean](lean:Development/AbelianVarietyTheory/Definitions/ModuliSpaces/IsSymm.lean#L47). The relation `KSRel` in the same file ties a derivation to a period matrix $\Theta$, so $\kappa$ is probably a Kodaira-Spencer map. We have not unfolded step 1.

Seven hypotheses are never used: the theorem of the cube (input 9), $p + q \ge 1$, the symplectic basis condition, $a(w) = w_0$, $a(w') = \bar w_0$, the generation of $\mathcal{O}_E$ by $a$, and the finite type of $R$ over $o$. The proof binds them to `_`.
