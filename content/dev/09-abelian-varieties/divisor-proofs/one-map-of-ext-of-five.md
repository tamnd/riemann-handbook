---
id: one-map-of-ext-of-five
title: The conjugate theta lift is a cusp form times a phase
kind: theorem
decl: GlobalTheory.GalOne.oneMap_of_ext_ofFive
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.CoefMapNormEquivariantBasisOfFive
covers: 382
status: drafted
drafted_by: writer@claude
---
This theorem says that the theta lift of a form, after a complex embedding $\sigma$ of the coefficients, is the adelic function of a cusp form, up to a phase function $u$, a central element $z$ and a constant of absolute value $1$. Its one caller is [`oneMapConj5`](/entry/one-map-conj5/), which chooses the extension $\sigma'$ of $\sigma$ and checks the hypotheses. The chain above it ends at the theorem [`nonempty_hyps_definite_side_of_closed_bound`](/step/nonempty-hyps/) of the [unitary hypotheses chapter](/proof/unitary-hypotheses/).

## Statement

Fix a finite group $G$, a core $T$, a real datum $R$ with $\mathrm{Core5}(R, F)$ (five conditions: level, group, family, models, theta), a tie `FWTie`, an index $i$, and a pinned datum $O$ of type `OM T R i`. Let $V = V_i$ and $W = W_i$ be the two hermitian spaces `Vc D i` and `Wc D i`. Let $\sigma$ be an embedding of the coefficient field $L$ into $\mathbb{C}$, and let $\sigma'$ be an embedding of the larger field of $O$ with $\sigma' \circ j_L = \sigma$. Let $s$ be the restriction of $\sigma'$ to the base field, and assume $T.V_{i+1}(s) = W$. Assume also:

- `RepsR`: $h$ is a set of representatives of finitely many classes in the adelic group of $V$;
- `CoefficientBaseChange`, `IsConjForms`: the coefficient maps for $L$, for the field of $O$ and for $\sigma$ are compatible;
- `ConjW`, `LiftData`: $\omega$ is a Weil representation for the characters $(\mu', \mu'\eta'^{-1})$, $f$ is a theta vector, and $\vartheta$ (the Lean `thP`) is the theta lift built from them.

**Theorem.** There are $u \colon G(\mathbb{A}, W) \to \mathbb{C}$, $z$ in the center of $G$ and $\kappa \in \mathbb{C}$ with $|\kappa| = 1$ such that:

1. $u$ is a phase function (`PhaseFun`): $|u| = 1$, $u$ is left invariant under the rational points, and right invariant under the archimedean part and under the level subgroup;
2. for each $g \in G$, each level lift $k$ of $g$, each cusp form $f$ and each $h$: $u(h)\, \varphi(g \cdot f)(h) = \sigma(\chi(g))\, u(hk)\, \varphi(f)(hk)$, where $\varphi$ is `phiC` and $\chi$ is the character of `R.FW i`;
3. if $x_0 = \sum_k a_k f_k$ in the sense of `IsClassSum`, then for all $g$
$$\kappa\, \vartheta(j x_0)(v_0)(g) = \sum_k \sigma(a_k)\, u(g)\, \varphi(z \cdot f_k)(g).$$

## Proof

1. `GalOne.Facts.factsAt_ofFive` gives $\mathrm{res}(\sigma) = s$. `tie.laws.cUnit` gives $|c_E| = 1$.
2. `FrameConst.exists_frAtEmb_ofFive` gives a function `cst` of absolute value $1$ on the components.
3. `identity_of_frConst_ofFive` gives $c_0$ with $|c_0| = 1$, the central element $z$ and an identity between theta integrals over the $h_j$ and values of the cusp forms $z \cdot f_k$.
4. `IoCmp.ioAt_of_conj_ofFive` gives a constant $\mathrm{ph}$ with $|\mathrm{ph}| = 1$.

Then $u(g) = \mathrm{cst}(g)/c_E(g)$, read through the dictionary `dictS`, and $\kappa = \mathrm{ph}\, c_0$. Clause 1 is `comp_inv_ofFive`. Clause 2 is `Equivar.eqAt_of_frAtEmb_ofFive`, with `hR.grp.chiW` to bring $\chi(g)$ into the base field. For clause 3, `theta_eq_classSum_of_conjugate` writes $\vartheta(j x_0)$ as a sum over the $h_j$, `exists_values_ofFive` matches the values through the coefficient maps, `FieldBC.actLev_and_actBC` moves $z$ through the base change, and step 3 closes. The rest is bookkeeping.

## In the Lean code

The theorem is in [CoefMapNormEquivariantBasisOfFive.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/CoefMapNormEquivariantBasisOfFive.lean#L2760). `PhaseFun`, `IsClassSum` and `LiftData` are in [ReadingsExistRow.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ReadingsExistRow.lean#L73), `ConjW` in [FrAtEmb.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/FrAtEmb.lean#L28), and `phiC` in [FWExist.lean](lean:Formalism/LocalToGlobal/IndefiniteReal/FWExist.lean#L366). We have not unfolded `OMDat`, `Pins`, `IsThClsD`, `IsBC` or the statements of the lemmas in steps 2 to 4.

Clause 2 is the predicate `EquivBy` of the caller, written out.
