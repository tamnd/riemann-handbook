---
id: exists-analytic-chart
title: The analytic chart at a complex point
kind: theorem
decl: GlobalTheory.AnVal.exists_analytic_chart
module: Development.AbelianVarietyTheory.Proofs.CuspFormEvaluations.ExistsAnalyticBiextensionChartComplexPoint
covers: 325
status: drafted
drafted_by: writer@claude
---
At a complex point of the moduli space, this theorem builds a formal chart of the universal abelian scheme from a complex uniformization. In this chart the formal group law is additive. The germ of a section of $L^k$ is the Taylor series of the theta function that represents the section. The [statement form](/entry/exists-analytic-biextension-chart-complex-point/) restates the theorem. Its only user is [`harm_nab_eq_polyDeriv`](/entry/harm-nab-eq-poly-deriv/).

## Statement

Let $E$ be a CM field. Let $X_o$ be the moduli scheme of a datum over $E$ and a level, with universal abelian scheme $A$, line bundle $L$ and $\mathcal{O}_E$ action. Let $c$ be a coefficient datum with field $c.F \subset \mathbb{C}$. Suppose that the star operation on $\mathcal{O}_E$ is the conjugation of the datum.

Let $y$ be a framed complex point (`FrPt`). It is a point $x$ of $X_o$ over $\mathbb{C}$ with tangent vectors $u_\ell$ of $A_x$ at $0$, one for each index $\ell = (\tau, i)$ with $\tau \colon E \to \mathbb{C}$ and $i < m_\tau$, and a generator of $L$ at $x$. Let $\Phi$ be an analytic point (`AnPt`) over $y$ of dimension $g$, with embeddings $t_1, \dots, t_g$ of $E$ and a bijection $\epsilon$ from $\{1, \dots, g\}$ to the indices $\ell$. The data of $\Phi$ are:

- a surjective holomorphic homomorphism $e \colon \mathbb{C}^g \to A_x(\mathbb{C})$ whose kernel is a lattice $\Lambda$;
- a Hermitian matrix $H$, a character $\chi$ of $\Lambda$ with $|\chi| = 1$, and nonvanishing holomorphic trivializations $f_j$ of $e^*L$ with $f_j(z) = \chi(a) \exp(\pi H(z, a) + \tfrac{\pi}{2} H(a, a)) f_j(z + a)$ for $a \in \Lambda$;
- $e(t(a) z) = a \cdot e(z)$, where $t(a)$ multiplies the coordinate $k$ by $t_k(a)$, and $H(t(a) z, w) = H(z, t(\bar a) w)$;
- the derivative of $e$ at $0$ in the coordinate direction $\epsilon^{-1}(\ell)$ is $u_\ell$.

A section $F$ of $L^k$ at $x$ *reads as* $\theta \colon \mathbb{C}^g \to \mathbb{C}$ if $F(e(z)) = \theta(z) f_j(z)^k$ in each trivialization.

**Theorem.** There is a chart $C$ at $y$ (`ChartAt`) of dimension $d = g$ with gauge $h = 0$ such that:

1. the formal group law is $F_i(X, Y) = X_i + Y_i$;
2. the tangent vector $u_\ell$ has coordinates $\delta_{i, \epsilon^{-1}(\ell)}$;
3. for each $k$ and each section $F$ that reads as $\theta$, the germ of $F$ in $C$ (`IsGerm`) is the Taylor series $\sum_n \partial^n \theta(0) z^n / n!$.

## Proof

The chart is `AnPt.chartOf`. Its formal data are `anFB t`: the additive law, the action of $a$ by $t(a)$, and all cocycles equal to $1$. Its jets are the jets of $e$ at $0$ (`AnPt.jx`). Its tangent vectors are `anUvec ε`. Two lemmas give the rest:

1. `exists_analyticFrame_jetPair_isAnE` gives a biextension frame that reads as products of the $f_j$.
2. `exists_normalisedIso_reading_one_analyticFrame` gives a primitive generator `wP`.

The chart axioms come from `cmFrame_exponential_jets_isChart`. The frame axioms come from `isFrame_of_isAnE`. The gauge axiom is `anFB_canon`, and the rigidification comes from `analytic_line_bundle_frame_eq_appellHumbert`. Claims 1 and 2 are true by definition. Claim 3 is `isGerm_tay_of_rd`. Its helper lemmas are not unfolded here.

## In the Lean code

The theorem is in [ExistsAnalyticBiextensionChartComplexPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/ExistsAnalyticBiextensionChartComplexPoint.lean#L73). `ChartAt` and `IsGerm` are in [ThGerm.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThGerm.lean#L189). `AnFr`, `AnPt` and the reading `AnFr.Rd` are in [ThConst.lean](lean:Development/AbelianVarietyTheory/Definitions/ThetaValues/ThConst.lean#L33). The Taylor series `tay θ 0` is in [Taylor.lean](lean:ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/TaylorDiscriminants/Taylor.lean#L145).

The statement carries an equality $d = g$ and renames the variables of the germ along it. The proof takes $d = g$ by definition, and `rename_cast_refl` removes the renaming. The three goals close by `first | rfl | simp ...`.
