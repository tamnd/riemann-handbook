---
id: abstract-count
title: An abstract bound for the Selmer lengths by points of the deformation ring
kind: theorem
decl: UpperTheory.V.UnitaryThreeInertia.abstract_count
module: Development.AutomorphicArithmetic.AutomorphicVarieties.UnitaryThreeDeformations.AbstractCount
covers: 483
status: drafted
drafted_by: writer@claude
---
This theorem is the abstract form of [the case V count](/entry/count-v-of-finiteness-duality-euler-host/). For a frame of three-dimensional representations near the reducible point $r_0$, it bounds the lengths of the Selmer-type modules by a sum of valuations of trace differences at finitely many characteristic zero points. The parent entry applies it to the host frame. The bound itself comes from the graded algebra lemmas $\mathrm{LemmaM}$ and $\mathrm{LemmaM'}$, which [`main_holds`](/entry/main-holds/) proves.

## Statement

Let $\mathcal{O}$ be a complete discrete valuation ring of characteristic zero, finite over $\mathbb{Z}_l$, with finite residue field. Let $e_{\mathcal{O}}$ be the length of $\mathcal{O}/l\mathcal{O}$, that is, the ramification index. Let $F$ be a frame with groups $G$ and $\Gamma$, a character $\eta$ and a character $\Psi$, and let $r_0$ be its reducible residual point and $r_z$ the image of $r_0$ over $\overline{\mathbb{Q}}_l$. Let $u \colon \Gamma \to \mathrm{GL}_3(R)$ be a universal deformation for a marked element $g_1$ (`IsUniv`). The torus $\mathrm{diag}(t, 1, t^{-1})$ acts on $R$ by conjugation, and $R_j$ is the part of weight $j$. Let $\varphi \in \Gamma$ and let $\mathrm{Good}$ be a property of representations. For $a \in \mathcal{O}$, let $\ell(a)$ be the length of the module $\mathrm{Sha}_{\mathcal{O}}(a)$, a submodule of $H^1$ with coefficients in $\mathcal{O}/(a)$, on which the group acts by $\Psi^{-1}$ (`shaLen`).

**Theorem.** Assume $\mathrm{LemmaM}$ and $\mathrm{LemmaM'}$, and the frame conditions `Ok`, `LocVan`, `Count`, `VanE`, `Cl1` and `Xpp`. Suppose that $R_0$ is finite over $\mathcal{O}$, that each point of $u$ of type I is Good, and that each characteristic zero Good point $r$ of type I is rigid with $\operatorname{tr} r(\varphi) \ne \operatorname{tr} r_z(\varphi)$. Then there are characteristic zero Good points $r_1, \dots, r_n$ of type I, pairwise non-isomorphic on $\ker \eta$, and an integer $V$, with $\ell(a) \le V$ for all $a \ne 0$ and

$$V \le 2 e_{\mathcal{O}} \sum_{i=1}^{n} v_l\bigl(\operatorname{tr} r_i(\varphi) - \operatorname{tr} r_z(\varphi)\bigr).$$

Here type I means irreducible on $\ker \eta$, and $v_l(x) = -\log\lVert x\rVert / \log l$. We have not unfolded `Ok`, `LocVan`, `VanE`, `Cl1`, `Xpp` or `Rigid`.

## Proof

1. `exists_adapted` gives a minimal presentation $W$ of $R$ adapted to the weights. `hasOrigin` gives the origin, which sends $u$ to $r_0$, and `exists_relations` gives the relations. Each weight lies in $[-2, 2]$.
2. Let $a = \operatorname{tr} u(\varphi) - \operatorname{tr} r_0(\varphi)$. It has weight $0$ and vanishes at the origin. Each point $\xi$ of the graded subalgebra gives a unique representation (`existsUnique_isPtHom`), and $\xi(a)$ is its trace difference.
3. A point that is nonzero on some negative weight and on some positive weight is of characteristic zero and of type I (`isPtHom_sign`, `typeI_of_twoSigned`). A point that is zero on all negative or on all positive weights equals the origin (`eq_rz_of_diag`, `isPtHom_act`).
4. `Count` and `finrank_H1L_le` bound the number of generators in each weight. Rigidity gives that each tangent vector at a two-signed point lies along the torus orbit (`tangent_eq_orbit`), and that $\xi(a) \ne 0$.
5. The main step is `Abs.coord_count`, with the norm bound `norm_bound_of_integral_values` and `tangent_coord_eq_zero_of_nonpos_weight` (from `VanE`). It gives the points, $V$ and the inequality.
6. `conj_of_matIso` turns isomorphic points into points in one torus orbit, which gives distinctness. `mprime_coord` gives the bound on $\ell(a)$.

## In the Lean code

The theorem is in [AbstractCount.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/AbstractCount.lean#L25). `Abs.coord_count` is in [AbsCoord.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/AbsCoord.lean#L68). `shaLen` is in [FiniteResidue.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeDeformations/FiniteResidue.lean#L10).

The property Good is free. The theorem asks only that the points of type I are Good, and it uses Good only to reach the rigidity hypothesis.
