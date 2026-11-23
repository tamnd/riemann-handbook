---
id: has-ext
title: Extension from a setup, by gluing the charts
kind: theorem
decl: GlobalTheory.Desc.Setup.hasExt
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.HasExtOfSetup
covers: 427
status: drafted
drafted_by: writer@claude
---
This theorem glues the local semi-abelian models of a `Setup` into one semi-abelian scheme over $\operatorname{Spec} R$. Its second name [`hasExt_of_setup`](/entry/has-ext-of-setup/) is used by [`hasExt_awayMap_of_charts`](/entry/has-ext-away-map-of-charts/). The proof chains four statements, each proved in its own file.

## Statement

A `Setup` $\sigma$ has these fields, grouped by purpose.

- **Base.** A noetherian integrally closed domain $R$ and $f \in R$, $f \neq 0$.
- **Generic object.** An integral abelian scheme $A$ over $\operatorname{Spec} R_f$ and an ample Cartier divisor $D$ on $A$.
- **Charts.** For each $x \in \operatorname{Spec} R$, a chart at $x$ (see [`hasExt_opensRange`](/entry/has-ext-opens-range/)), with complete regular local ring $R_x$ and integral semi-abelian scheme $G_x$ over $R_x$.
- **Chart maps.** A flat ring map $\rho_x \colon R \to R_x$ that gives the chart map; the open $V_x \subseteq G_x$ where $\rho_x(f)$ is a unit; a map $\varphi_x \colon V_x \to A$ with $V_x = A \times_{\operatorname{Spec} R} \operatorname{Spec} R_x$, compatible with the generic identification of the chart; and a map of function fields $\theta_x \colon K(A) \to K(G_x)$ compatible with $\varphi_x$.
- **Divisors.** A Cartier divisor $D_{1,x}$ on $G_x$ that restricts to the pullback of $D$ on $V_x$, has local equation $1$ at each codimension one point over $V(f)$, and is ample.

**Theorem.** For each `Setup` $\sigma$, the abelian scheme $A$ extends to a semi-abelian scheme over $\operatorname{Spec} R$.

## Proof

1. `GlobalTheory.T.abelianSchemeDescentData_charts_common`: $\sigma$ satisfies `Common`. This says that two charts agree near a common point. Take charts at $x$ and $x'$ and maps $u \colon R_x \to \Omega$, $u' \colon R_{x'} \to \Omega$ to a field that agree on $R$, with $\ker u'$ the maximal ideal. Then there are a regular local domain $E$, flat maps $R_x \to E$ and $R_{x'} \to E$ that agree on $R$, a residue map $E \to \Omega$ through which $u$ and $u'$ factor, and a semi-abelian scheme $H$ over $E$ that is the group pullback of both $G_x$ and $G_{x'}$, compatibly with the maps $\theta_x$, $\theta_{x'}$.
2. `GlobalTheory.T.nonempty_descentSeparatedEmbedding`: given `Common`, there is an embedding datum `Emb`. This is an integral scheme $P$, separated over $\operatorname{Spec} R$, with an open embedding of $A$ as $P \times_R \operatorname{Spec} R_f$, and maps $G_x \to P$ such that $G_x \to P \times_R \operatorname{Spec} R_x$ is an open immersion, compatible with the $\varphi_x$.
3. `GlobalTheory.T.exists_localGroup_range_union_closedFibres`: let $U \subseteq P$ be the set of images of the points of the closed fibres of all $G_x$. For each $x$ there is $g \in R$ with $g \notin x$ and a smooth quasi-compact group scheme $H$ over $\operatorname{Spec} R_g$ with an open immersion $H \to P$ over $\operatorname{Spec} R$, whose group law agrees with that of $A$, and whose image is $U$ above $D(g)$ (`LocGrp`).
4. `GlobalTheory.T.extendsToSemiAbelian_of_local_groups`: from the data of steps 1 to 3, $A$ extends over $\operatorname{Spec} R$.

## In the Lean code

The theorem is at [HasExtOfSetup.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasExtOfSetup.lean#L15). `Setup`, `Common`, `Emb` and `Emb.LocGrp` are in [SubsetSpanBy.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SubsetSpanBy.lean#L123). The four lemmas are statement forms of `setup_common`, `nonempty_emb`, `UnionLocal.exists_locGrp_range_eq` and `Emb.hasExt_of_locGrp`. We read their statements, not their proofs. The proof here only chains them. This proof does not read the fields of $\sigma$ itself. It passes $\sigma$ to the four lemmas.
