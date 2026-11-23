---
title: Potential good reduction and projectivity
decls:
  - GlobalTheory.HTPotGood.potGood
  - GlobalTheory.T.harrisTaylorModuliObject_potentiallyGoodReduction
  - GlobalTheory.UPel.HT.isProper_model_of_compact
  - GlobalTheory.T.harrisTaylor_integralModel_isProper_of_compact
  - GlobalTheory.UPel.HT.Model.isProjOver_of_compactB
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Potential good reduction and projectivity

The model of Definition 8.1.4 is quasi-projective. This section shows that it is projective over a noetherian domain of characteristic $0$ when the datum is *compact*: either few embeddings $\tau_i$ are used, or $O$ is close to a division algebra and $n$ is small. The proof has three steps. First, every object over the fraction field of a complete discrete valuation ring of characteristic $0$ has potentially good reduction. Second, the valuative criterion then gives properness: a point over the fraction field extends, after a finite extension, to the ring. Third, a quasi-projective and proper scheme over a noetherian ring is projective. Projectivity is used by [the Kodaira-Spencer map of weight one](/entry/kodaira-spencer-of-weight-one/).

We keep the datum $D$ of Definition 8.1.1, with the CM field $F$, the integers $a$, $m$, $n$, the order $O$ of rank $m^2 [F : \mathbb{Q}]$ and the lattice $\Lambda$ of rank $mn [F : \mathbb{Q}]$, and the objects $o = (A, \iota, P, \eta)$ of Definition 8.1.3.

### Compact data

**Definition 8.31.1 (Compact datum).** The order $O$ is of *division type* if for every $x \neq 0$ in $O$ there are $y \in O$ and an integer $c \neq 0$ with $x y = c$. The datum $D$ is *compact* if
$$2a < [F : \mathbb{Q}] \quad \text{or} \quad \big(O \text{ is of division type and } n < 2m\big).$$

Lean: `GlobalTheory.UPel.HT.Datum.CompactB` (also `GlobalTheory.UPel.HT.Datum.Compact` and `GlobalTheory.UPel.HT.Datum.IsDivision`).

If $O$ is of division type, then $O \otimes \mathbb{Q}$ is a division algebra: $x y = c$ gives $x \cdot c^{-1} y = 1$. For example, $D$ is compact when $a = 0$, and when $a = 1$, $m = n$ and $O$ is of division type, since $n < 2n$; this is the case of Harris and Taylor. It is not compact when $m = 1$, $n \geq 2$ and $[F : \mathbb{Q}] \leq 2a$, since then $n \geq 2 = 2m$.

### Potential good reduction

Let $V$ be a complete discrete valuation ring with fraction field $K$ of characteristic $0$, and let $A$ be a commutative group scheme over $K$. For a ring map $W \to L$ with $K \to L$, a group scheme $G$ over $W$ is a *model of $A$ over $L$* if there is an isomorphism of group schemes $G_L \cong A_L$.

**Definition 8.31.2 (Potentially good reduction).** The group $A$ has *potentially good reduction over $V$* if there are a complete discrete valuation ring $W$, finite over $V$, with a local map $V \to W$, and its fraction field $L$ with a map $K \to L$ compatible with $V \to W \to L$, and an abelian scheme $G$ over $W$ that is a model of $A$ over $L$.

Lean: `GlobalTheory.SS.PotModel` (also `GlobalTheory.SS.IsModel`).

This is the notion of [Néron models and good reduction](/learn/abelian-varieties/#neron-models-and-good-reduction) of Volume 1, phrased without Néron models: $G$ is then the Néron model of $A_L$.

**Definition 8.31.3 (Lie multiplicity).** Let $G$ be a group scheme over $S$ with an action $\iota$ of $\mathcal{O}_F$, let $x : \operatorname{Spec} k \to S$ be a geometric point, and let $\sigma : \mathcal{O}_F \to k$ be a ring map. A tangent vector $v$ of $G_x$ at the origin is a *$\sigma$-eigenvector* if $\iota(a)_* v = \sigma(a) v$ for all $a$. The *Lie multiplicity* of $\sigma$ at $x$ is $r$ if there are $r$ such eigenvectors such that every $\sigma$-eigenvector is a unique $k$-linear combination of them.

Lean: `ReciprocityTheory.ChartRestriction.G.Geo.Tor.LieMult` (also `ReciprocityTheory.ChartRestriction.G.Geo.Tor.IsLieEigen`).

So the Lie multiplicity of $\sigma$ is the dimension of the $\sigma$-eigenspace of $\mathcal{O}_F$ on $\operatorname{Lie}(G_x)$.

### Inputs

We use the following results; results 2 and 5 are criteria for potentially good reduction.

1. (A vanishing multiplicity.) Assume $2a < [F : \mathbb{Q}]$. Let $o$ be an object of level $N$ over $s : S \to \operatorname{Spec} R$, $k$ an algebraically closed field of characteristic $0$, and $x : \operatorname{Spec} k \to S$ with $s x = \operatorname{Spec} \beta$ for a ring map $\beta : R \to k$. Then there is $\sigma : \mathcal{O}_F \to k$ of Lie multiplicity $0$ at $x$ for the action of $\mathcal{O}_F \subseteq O$ on $A$. (`GlobalTheory.T.exists_embedding_lie_multiplicity_zero_char_zero`, `GlobalTheory.HTLie.exists_lieMult_zero`)
2. (Criterion by Lie multiplicity.) Let $V$, $K$ be as above, $F$ a number field, $A$ an abelian scheme over $K$ with an action of $\mathcal{O}_F$, $\Omega$ an algebraically closed field, $g : K \to \Omega$ a ring map, and $\sigma : \mathcal{O}_F \to \Omega$ of Lie multiplicity $0$ at $\operatorname{Spec} g$. Then $A$ has potentially good reduction over $V$. (`GlobalTheory.T.potentialGoodReduction_of_lieMult_zero`, `GlobalTheory.PotGoodLie.potGood_of_lieMult_zero`)
3. (Dimension.) An abelian scheme over a field is smooth of some relative dimension $g$. (`GlobalTheory.AbVarRelDim.exists_relDim`)
4. (Dimension of objects.) Let $K$ be a field, $\beta : R \to K$, and $o$ an object of level $N$ over $\operatorname{Spec} \beta$ with $A$ smooth of relative dimension $g$. Then $2g$ is the rank of $\Lambda$. (`GlobalTheory.T.two_mul_relDim_eq_finrank_harrisTaylor_lattice`, `GlobalTheory.UPel.HT.two_mul_relDim_eq_finrank`)
5. (Criterion by a division order.) Let $V$, $K$ be as above and $A$ an abelian scheme over $K$, smooth of relative dimension $g$. Let $O'$ be a ring, free of finite rank over $\mathbb{Z}$ and of division type, that acts on $A$ by homomorphisms: $1$ acts as the identity, $a b$ acts as $\iota(a) \circ \iota(b)$ and $a + b$ as $\iota(a) + \iota(b)$. If $g$ is less than the rank of $O'$, then $A$ has potentially good reduction over $V$. (`GlobalTheory.T.potentialGoodReduction_of_order_leftAction`, `GlobalTheory.potModel_of_intDivOrder_leftAction`)

**Theorem 8.31.4 (Potentially good reduction).** Let $D$ be compact, $b$ a base for $D$ over $R$, and $N \geq 0$. Let $V$ be a complete discrete valuation ring with fraction field $K$ of characteristic $0$, $\beta : R \to K$ a ring map, and $o$ an object of level $N$ over $\operatorname{Spec} \beta$. Then the abelian scheme $A$ of $o$ has potentially good reduction over $V$.

Lean: `GlobalTheory.HTPotGood.potGood` (also `GlobalTheory.T.harrisTaylorModuliObject_potentiallyGoodReduction`, a second name).

*Proof.* Suppose first that $2a < [F : \mathbb{Q}]$. Let $\Omega$ be an algebraic closure of $K$ and $x = \operatorname{Spec}(K \to \Omega)$; then $x$ lies over $\operatorname{Spec}$ of $R \to K \to \Omega$. Result 1 gives $\sigma : \mathcal{O}_F \to \Omega$ of Lie multiplicity $0$ at $x$, and result 2 concludes.

Suppose now that $O$ is of division type and $n < 2m$. By result 3, $A$ is smooth of some relative dimension $g$, and by result 4 and Definition 8.1.1, $2g = mn [F : \mathbb{Q}]$. Since $n < 2m$ and $m, [F : \mathbb{Q}] > 0$,
$$2g = mn[F : \mathbb{Q}] < 2m^2 [F : \mathbb{Q}],$$
so $g$ is less than the rank $m^2 [F : \mathbb{Q}]$ of $O$. The action $\iota$ of $O$ on $A$ satisfies the conditions of result 5, which concludes. $\square$

### Properness and projectivity

We use, besides the pullback of objects along a map of schemes and the composition of maps of objects, the following results.

6. (A valuative criterion.) Let $R$ be a noetherian domain of characteristic $0$ and $s : X \to \operatorname{Spec} R$ quasi-projective and flat. Suppose that for every complete discrete valuation ring $V$ with fraction field $K$ of characteristic $0$, every ring map $\beta : R \to V$ and every $x : \operatorname{Spec} K \to X$ over $\operatorname{Spec} R$, there are a local domain $W$ with fraction field $L$, a local map $V \to W$, a map $K \to L$ compatible with $V \to W \to L$, and $f : \operatorname{Spec} W \to X$ that agrees with $x$ on $\operatorname{Spec} L$. Then $s$ is [[proper|9537RKBZPP]]. (`GlobalTheory.T.isProper_of_lift_completeDvr_charZero`, `GlobalTheory.ValuativeFlat.isProper_of_lift_dominating`)
7. (Models and pullbacks.) Let $G$ over $W$ be a model of $A$ over $L$, and let $A'$ over $L$ be a group pullback of $A$ along $\operatorname{Spec} L \to \operatorname{Spec} K$ (Definition 8.2.5). Then $A'$ is a group pullback of $G$ along $\operatorname{Spec} L \to \operatorname{Spec} W$. (`GlobalTheory.T.isGrpPullback_of_group_scheme_model_base_change`, `GlobalTheory.SS.exists_isGrpPullback_of_isModel`)
8. (Extension of objects.) Let $W$ be a discrete valuation ring with fraction field $L$, $\gamma : R \to W$ a ring map, $o$ an object of level $N$ over $\operatorname{Spec} L \to \operatorname{Spec} R$, and $G$ an abelian scheme over $W$ with a map making $A$ a group pullback of $G$ along $\operatorname{Spec} L \to \operatorname{Spec} W$. Then there are an object $o'$ of level $N$ over $\operatorname{Spec} \gamma$ and a map of objects $o \to o'$ over $\operatorname{Spec} L \to \operatorname{Spec} W$. (`GlobalTheory.T.harrisTaylorObject_extends_over_dvr_of_abelianModel`, `GlobalTheory.HTObjExt.extends_obj`)
9. (Projectivity.) Let $R$ be noetherian and $s : X \to \operatorname{Spec} R$ quasi-projective and proper. Then $s$ is projective: there is a closed immersion $i : X \to \mathbb{P}^M_R$ over $R$. (`GlobalTheory.UPel.isProjOver_of_isQProjOver_of_isProper`, `GlobalTheory.SchemeWords.isProjOver_iff`)

Result 9 holds since an immersion with proper source into a separated scheme is proper (Hartshorne, *Algebraic Geometry*, Corollary II.4.8), so its image is closed.

**Theorem 8.31.5 (Properness).** Let $R$ be a [[noetherian|0670T59HGE]] domain of characteristic $0$, $b$ a base for $D$ over $R$, $N \geq 0$, and $(X, s, u)$ a model of level $N$ over $b$. If $D$ is compact, then $s : X \to \operatorname{Spec} R$ is proper.

Lean: `GlobalTheory.UPel.HT.isProper_model_of_compact` (also `GlobalTheory.T.harrisTaylor_integralModel_isProper_of_compact`, a second name).

*Proof.* The map $s$ is quasi-projective and [[smooth|EXKGG9X6J0]] (Definition 8.1.4), so flat, and we check the condition of result 6. Let $V$, $K$, $\beta : R \to V$ and $x : \operatorname{Spec} K \to X$ be as there. Pulling $u$ back along $x$ gives an object $o_K$ of level $N$ over $\operatorname{Spec}(R \to V \to K)$ with a map of objects $o_K \to u$ over $x$. By the theorem above, $A_K$ has potentially good reduction: there are $W$, $L$ and an abelian scheme $G$ over $W$ that is a model of $A_K$ over $L$, and $W$ is a local domain with $V \to W$ local. Pull $o_K$ back to an object $o_L$ over $\operatorname{Spec} L$, with a map of objects $o_L \to o_K$. By result 7, $A_L$ is a group pullback of $G$, and by result 8 there are an object $o_W$ over $\operatorname{Spec} W$ and a map of objects $o_L \to o_W$. Since $X$ represents objects, there is $f : \operatorname{Spec} W \to X$ with a map of objects $o_W \to u$ over $f$. Now $o_L$ has two maps of objects to $u$: through $o_W$, over $f$ restricted to $\operatorname{Spec} L$, and through $o_K$, over $x$ restricted to $\operatorname{Spec} L$. By the uniqueness in Definition 8.1.4 both maps $\operatorname{Spec} L \to X$ are the map that classifies $o_L$, so $f$ agrees with $x$ on $\operatorname{Spec} L$. $\square$

**Theorem 8.31.6 (Projectivity).** Let $R$ be a noetherian domain of characteristic $0$, $b$ a base for $D$ over $R$, $N \geq 3$ prime to $p$, and $(X, s, u)$ a model of level $N$ over $b$. If $D$ is compact, then there is a closed immersion $X \to \mathbb{P}^M_R$ over $R$ for some $M$.

Lean: `GlobalTheory.UPel.HT.Model.isProjOver_of_compactB`.

*Proof.* The map $s$ is quasi-projective by Definition 8.1.4 and proper by the previous theorem. Result 9 concludes. $\square$

**Remark 8.31.7 (Formalization).** The potential good reduction theorem is in [HarrisTaylorModuliObjectPotentiallyGoodReduction.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorModuliObjectPotentiallyGoodReduction.lean#L22), properness in [HarrisTaylorIntegralModelIsProperOfCompact.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorIntegralModelIsProperOfCompact.lean#L27) and projectivity in [IsProjOverOfCompactB.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProjOverOfCompactB.lean#L10). In the projectivity theorem the hypotheses $N \geq 3$ and $N$ prime to $p$ are not used ([line 11](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProjOverOfCompactB.lean#L11)). The two definitions of a compact datum are the same formula, and their equivalence at [CompactBIffCompact.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/CompactBIffCompact.lean#L12) is proved by reflexivity. The wrappers of the second names raise the heartbeat limit and try three tactics to apply one lemma, for example at [lines 15 to 17](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/HarrisTaylorIntegralModelIsProperOfCompactStatement.lean#L15) of the properness wrapper. Results 1 to 9 are cited by their statements. Result 6 asks less than the valuative criterion: only complete $V$ with fraction field of characteristic $0$, and only an extension after a local extension $V \to W$.

## Notes and references

The models of this chapter feed [the Kodaira-Spencer map of weight one](/entry/kodaira-spencer-of-weight-one/): their existence and smoothness (Sections 8.1 to 8.18), their tangent spaces and Kodaira-Spencer counts (Sections 8.19 to 8.22), their complex points (Section 8.24), the isogenies of type $T_j$ (Sections 8.27 to 8.29), the comparison of de Rham homology with Dieudonné theory (Sections 8.25, 8.26 and 8.30) and projectivity (this section). That theorem is used in the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).

- R. Kottwitz, "Points on some Shimura varieties over finite fields", J. Amer. Math. Soc. 5 (1992), §5. The PEL moduli problem, its representability by a smooth quasi-projective scheme, and the Lie condition (the Kottwitz condition). Here the problem is set up for the data of Harris and Taylor, and representability is proved through an auxiliary Siegel problem.
- M. Harris and R. Taylor, *The Geometry and Cohomology of Some Simple Shimura Varieties*, Ann. of Math. Stud. 151, Princeton Univ. Press, 2001, Chapter III. The integral models, the isogenies used for Hecke operators at $p$, and the compactness of the Shimura varieties for a division algebra. Our datum is more general, and the compactness hypothesis has two cases.
- D. Mumford, J. Fogarty and F. Kirwan, *Geometric Invariant Theory*, 3rd ed., Springer, 1994, Chapter 7. The Siegel moduli scheme with level structure, the input of Section 8.4.
- M. Schlessinger, "Functors of Artin rings", Trans. Amer. Math. Soc. 130 (1968), 208 to 222, §2. The gluing over fibre products of Artinian rings in Sections 8.2 to 8.5.
- J. Milnor, *Introduction to Algebraic K-Theory*, Ann. of Math. Stud. 72, §2. Projective modules and units over fibre products of rings, in Sections 8.2 and 8.3.
- A. Grothendieck, *Éléments de géométrie algébrique* IV, §8 and §17, and Corollaire 18.12.4. Limits, smoothness and finiteness conditions, in Sections 8.4 to 8.10.
- D. Mumford, *Abelian Varieties*, Chapter III and §21. Vanishing for ample line bundles and the theorem of the cube, in Sections 8.10 and 8.14.
- R. Hartshorne, *Algebraic Geometry*, Theorem III.2.7 and Corollary II.4.8. Vanishing above the dimension (Section 8.14) and properness of immersions (result 9 above).
- Yu. Zarhin, "A remark on endomorphisms of abelian varieties over function fields of finite characteristic", Math. USSR-Izv. 8 (1974), and L. Moret-Bailly, *Pinceaux de variétés abéliennes*, Astérisque 129 (1985), Chapitre IX. Zarhin's trick, in Sections 8.7 and 8.11.
- W. Messing, *The Crystals Associated to Barsotti-Tate Groups: with Applications to Abelian Schemes*, Lecture Notes in Math. 264, Springer, 1972. Grothendieck-Messing deformation theory, the classical form of the first-order statements of Sections 8.19 and 8.22.
- B. Mazur and W. Messing, *Universal Extensions and One Dimensional Crystalline Cohomology*, Lecture Notes in Math. 370, Springer, 1974, Chapter I. Rigidified and universal extensions, and the comparison of $H^1_{\mathrm{dR}}$ with the universal vector extension, the classical form of Section 8.30.
- J.-P. Serre and J. Tate, "Good reduction of abelian varieties", Ann. of Math. 88 (1968), Theorem 1. The criterion of Néron, Ogg and Shafarevich. The criteria of this section are of a different kind: they use the action of $\mathcal{O}_F$ or of $O$, not the Galois action on torsion points.
- A. Grothendieck, SGA 7 I, Exposé IX, Théorème 3.6. The semistable reduction theorem: every abelian variety over $K$ has potentially semi-abelian reduction.
