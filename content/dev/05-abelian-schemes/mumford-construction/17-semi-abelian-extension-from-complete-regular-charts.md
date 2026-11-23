---
title: Semi-abelian extension from complete regular charts
decls:
  - GlobalTheory.T.semiAbelian_descent_from_complete_regular_charts
  - GlobalTheory.Desc.descent_semiAbelian
  - GlobalTheory.T.exists_semiAbelianExtension_near_point
  - GlobalTheory.Desc.exists_hasExt_near
  - GlobalTheory.Desc.hasExt_opensRange
  - GlobalTheory.T.extendsToSemiAbelian_away_of_charts
  - GlobalTheory.Desc.hasExt_awayMap_of_charts
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Semi-abelian extension from complete regular charts

This section proves an extension criterion for abelian schemes. Let $S$ be a noetherian normal scheme and $A$ an abelian scheme over a dense open subscheme $X$ of $S$. Suppose that at every point $x$ of $S$, after the base change to a complete regular local ring that is an étale completion of $\mathcal{O}_{S,x}$, the abelian scheme extends to a semi-abelian scheme. Then $A$ extends to a semi-abelian scheme over $S$. The local extensions at the points come from Mumford's construction over complete bases, and the criterion turns them into an extension over the whole base. The result is used in [the step on characters from the literature](/step/every-character-of-literature/), where it extends abelian schemes over the open part of a moduli space. For semi-abelian degenerations see [semi-abelian degenerations and Mumford's construction](/learn/abelian-varieties/#semi-abelian-degenerations-and-mumfords-construction) in Volume 1.

### Charts and extensions

**Definition 4.17.1 (Chart).** Let $j : X \to S$ be a morphism of schemes, $A$ a group scheme over $X$ and $x$ a point of $S$. A *chart* of $(j, A)$ at $x$ consists of the following data.

1. A complete regular local domain $R_x$ of characteristic $0$ and a morphism $\xi : \operatorname{Spec} R_x \to S$ that maps the closed point to $x$.
2. The map $\mathcal{O}_{S,x} \to R_x$ induced by $\xi$ is flat, it satisfies $\mathfrak{m}_x R_x = \mathfrak{m}_{R_x}$, and the residue extension is finite. The composite $\mathcal{O}_{S,x} \to R_x \to \kappa(R_x)$ is formally unramified.
3. A semi-abelian group scheme $G_x$ over $R_x$.
4. A morphism $y : \operatorname{Spec} \operatorname{Frac} R_x \to X$ with $j \circ y = \xi \circ j_K$, where $j_K : \operatorname{Spec} \operatorname{Frac} R_x \to \operatorname{Spec} R_x$.
5. A morphism $\alpha$ from the generic fibre of $G_x$ to $A$ that makes this generic fibre the group pullback of $A$ along $y$.

Lean: `GlobalTheory.Desc.Chart`.

Condition 2 says that $R_x$ is a completion of an étale neighbourhood of $x$, up to a finite residue extension. So a chart is a semi-abelian extension of $A$ over a complete regular local ring that sees a formal neighbourhood of $x$.

**Definition 4.17.2 (Extension).** Let $j : X \to S$ be a morphism and $A$ a group scheme over $X$. We say that $A$ *extends along $j$* if there are a semi-abelian group scheme $G$ over $S$ and a morphism $e : A \to G$ that makes $A$ the group pullback of $G$ along $j$.

Lean: `GlobalTheory.Desc.HasExt`.

**Definition 4.17.3 (Relatively ample).** Let $A$ be a group scheme over $S$ and $L$ a line bundle on $A$. We say that $L$ is *relatively ample* if for every affine open $U \subseteq S$ there are $N \geq 1$ and sections $s_0, \dots, s_M$ of $L^N$ over $A_U$ with these properties: the loci $D(s_i)$ where $s_i$ does not vanish are affine and cover $A_U$, and on each $D(s_i)$ the functions $s_k / s_i$ generate the ring of functions over $\Gamma(U, \mathcal{O}_S)$.

Lean: `ReciprocityTheory.ChartRestriction.G.Out.RelAmple`.

So a relatively ample line bundle gives a closed embedding of $A_U$ into a projective space over $U$, for each affine $U$.

### Two inputs

The proofs use one published result. It is the extension of homomorphisms of semi-abelian schemes over a normal base (Faltings and Chai, *Degeneration of Abelian Varieties*, Springer 1990, Chapter I, Proposition 2.7).

**Theorem 4.17.4 (Extension of homomorphisms of semi-abelian schemes).** Let $V$ be a noetherian normal scheme, $l : W \to V$ a dense open immersion, and $G_1$, $G_2$ semi-abelian schemes over $V$. Then every homomorphism of group schemes $(G_1)_W \to (G_2)_W$ extends uniquely to a homomorphism $G_1 \to G_2$. In particular, if $G_1$ and $G_2$ restrict to the same group scheme over $W$, there is a unique isomorphism $G_1 \cong G_2$ compatible with the identifications over $W$.

Lean: `GlobalTheory.semiAbelianHomExtension_holds`.

**Lemma 4.17.5 (Factorial local rings).** Let $E$ be a regular local ring and $Y$ an integral scheme with a smooth morphism $Y \to \operatorname{Spec} E$. Then every local ring of $Y$ is a unique factorisation domain.

Lean: `GlobalTheory.Desc.ufm_stalk_of_smooth_regularLocal`.

*Proof.* A regular local ring is a regular ring, and a scheme smooth over a regular ring has regular local rings. A regular local ring is factorial (Auslander and Buchsbaum, Proc. Nat. Acad. Sci. USA 45, 1959). $\square$

### Extension over an affine base

**Theorem 4.17.6 (Extension away from a divisor).** Let $R$ be a noetherian, integrally closed domain and $f \in R$ with $f \neq 0$. Let $A$ be an abelian scheme over $\operatorname{Spec} R_f$ with a relatively ample line bundle $L$, and assume that $(\operatorname{Spec} R_f \to \operatorname{Spec} R, A)$ has a chart at every point of $\operatorname{Spec} R$. Then $A$ extends along $\operatorname{Spec} R_f \to \operatorname{Spec} R$.

Lean: `GlobalTheory.Desc.hasExt_awayMap_of_charts` (also `GlobalTheory.T.extendsToSemiAbelian_away_of_charts`, a second name).

*Proof.* *Step 1.* The ring $R_f$ is a domain, so $A$ is integral.

*Step 2: a symmetric ample divisor.* By an input, there is a Cartier divisor $\mathcal{D}$ on $A$ that is ample and symmetric, $[-1]^* \mathcal{O}(\mathcal{D}) \cong \mathcal{O}(\mathcal{D})$. Its construction uses $L$ and its relative ampleness; they are not used again.

*Step 3: standard form of the charts.* Choose a chart at each point $x$ of $\operatorname{Spec} R$, with ring $R_x$ and group $G_x$. By an input, $\xi$ is $\operatorname{Spec}$ of a flat map $\rho_x : R \to R_x$. Let $V_x \subseteq G_x$ be the open subset where $\rho_x(f)$ is a unit. Then $V_x$ is the base change of $A$ along $\rho_x$, through a morphism $\varphi_x : V_x \to A$ that agrees with the generic identification of the chart, and there is a map $\theta_x$ of function fields compatible with $\varphi_x$.

*Step 4: closure of the divisor.* The pullback of $\mathcal{D}$ to $V_x$ extends to a Cartier divisor $\mathcal{D}_{1,x}$ on $G_x$ with local equation $1$ at every point of $G_x$ over $V(f)$. So $\mathcal{D}_{1,x}$ has no vertical part. The closure of a Weil divisor is Cartier because the local rings of $G_x$ are factorial, by the lemma, since $G_x$ is smooth over the regular local ring $R_x$.

*Step 5: ampleness on the chart.* By an input, $\mathcal{D}_{1,x}$ is ample on $G_x$. This input uses the symmetry of $\mathcal{D}$, the completeness of $R_x$, characteristic $0$ and $\rho_x(f) \neq 0$.

*Step 6: gluing.* The data $R$, $f$, $A$, $\mathcal{D}$ and $(\rho_x, V_x, \varphi_x, \theta_x, \mathcal{D}_{1,x})$ for all $x$ form a setup for [the gluing theorem for charts](/entry/has-ext-of-setup/), proved in a later section. It gives the extension. $\square$

The idea of Steps 4 to 6 is that of Raynaud: an ample divisor without vertical part on each chart gives projective coordinates that are defined over $R$, and the extension is the closure of $A$ in the projective space they define.

**Theorem 4.17.7 (Extension over an affine open).** Let $S$ be a noetherian normal scheme, $j : X \to S$ a dense open immersion, $A$ an abelian scheme over $X$ with a relatively ample line bundle $L$, and assume that $(j, A)$ has a chart at every point of $S$. Let $R$ be a noetherian, integrally closed domain and $i : \operatorname{Spec} R \to S$ an open immersion with image $U$. Then the restriction of $A$ to $j^{-1}(U)$ extends along $j^{-1}(U) \to U$.

Lean: `GlobalTheory.Desc.hasExt_opensRange`.

*Proof.* *Step 1: a basic open.* Since $j$ has dense image, $i^{-1}(j(X))$ is a non-empty open subset of $\operatorname{Spec} R$. It contains a non-empty basic open $D(f)$, and $f \neq 0$ since $D(0)$ is empty.

*Step 2: the restriction.* Since $D(f)$ maps into $j(X)$, there is an open immersion $k : \operatorname{Spec} R_f \to X$ with $j \circ k = i \circ (\operatorname{Spec} R_f \to \operatorname{Spec} R)$. The base change $k^* A$ is an abelian scheme over $R_f$, and the pullback of $L$ is relatively ample.

*Step 3: restricted charts.* Let $x \in \operatorname{Spec} R$ and take the chart of $(j, A)$ at $i(x)$. Its map $\xi$ factors through $U$, since every point of $\operatorname{Spec} R_x$ specialises to the closed point and $U$ is open. The generic point of $\operatorname{Spec} R_x$ maps to the generic point of $\operatorname{Spec} R$, since $\xi$ is flat and $\operatorname{Spec} R$ is irreducible, and this point lies in $D(f)$. So the chart restricts to a chart of $(\operatorname{Spec} R_f \to \operatorname{Spec} R, k^* A)$ at $x$.

*Step 4.* The theorem on extension away from a divisor gives a semi-abelian $G$ over $\operatorname{Spec} R$ that extends $k^* A$.

*Step 5: the whole of $j^{-1}(U)$.* The scheme $j^{-1}(U)$ is noetherian and normal, and $\operatorname{Spec} R_f$ is a dense open subset of it. The restriction of $G$ to $j^{-1}(U)$ and the restriction of $A$ are semi-abelian schemes over $j^{-1}(U)$ that agree over $\operatorname{Spec} R_f$. By the theorem on extension of homomorphisms, they are isomorphic. So $G$, read over $U$ through $i$, extends $A|_{j^{-1}(U)}$. $\square$

### The extension criterion

**Theorem 4.17.8 (Local extensions).** Let $S$ be a noetherian normal scheme, $j : X \to S$ a dense open immersion, and $A$ an abelian scheme over $X$ with a relatively ample line bundle. Assume that $(j, A)$ has a chart at every point of $S$. Then every $s \in S$ has an open neighbourhood $U$ such that the restriction of $A$ to $j^{-1}(U)$ extends along $j^{-1}(U) \to U$.

Lean: `GlobalTheory.Desc.exists_hasExt_near` (also `GlobalTheory.T.exists_semiAbelianExtension_near_point`, a second name).

*Proof.* The irreducible components of a noetherian normal scheme are open. Let $Z$ be the one that contains $s$, and choose an affine open $U = \operatorname{Spec} R$ with $s \in U \subseteq Z$. Then $U$ is integral and normal, so $R$ is a noetherian, integrally closed domain. The theorem on extension over an affine open, with $i$ the inclusion of $U$, gives the extension. $\square$

**Theorem 4.17.9 (Semi-abelian extension from complete regular charts).** Let $S$ be a noetherian normal scheme, $j : X \to S$ a dense open immersion, $A$ an abelian scheme over $X$ and $L$ a relatively ample line bundle on $A$. Assume that $(j, A)$ has a chart at every point of $S$. Then there are a semi-abelian group scheme $G$ over $S$ and a morphism $e : A \to G$ that makes $A$ the group pullback of $G$ along $j$, with this property: for every point $x$ and every chart at $x$, with ring $R_x$, group $G_x$, map $\xi$ and generic identification $\alpha$, there is a morphism $\pi : G_x \to G$ that makes $G_x$ the group pullback of $G$ along $\xi$, such that $e \circ \alpha$ is the restriction of $\pi$ to the generic fibre.

Lean: `GlobalTheory.Desc.descent_semiAbelian` (also `GlobalTheory.T.semiAbelian_descent_from_complete_regular_charts`, a second name).

*Proof.* *Step 1: local extensions.* By the previous theorem, $S$ is covered by opens $U$ over which $A$ extends.

*Step 2: gluing.* By an input, extensions that exist locally on a noetherian normal scheme glue to an extension $(G, e)$ over $S$. Over the overlap of two opens, the two local extensions agree over the dense open part of $X$, so they agree by the theorem on extension of homomorphisms, and the identifications satisfy the cocycle condition by uniqueness.

*Step 3: the charts.* By a second input, for every chart at a point $x$ there is a morphism $\pi : G_x \to G$ with the stated properties. $\square$

The criterion is local in a strong sense. One needs a semi-abelian extension only over formal neighbourhoods of the points, and one gets an extension over $S$ with a canonical comparison to each local one. The ample line bundle is needed only to make the extension over affine pieces projective.

**Remark 4.17.10 (Formalization).** The second names are wrappers. In the theorem on extension away from a divisor ([ExtendsToSemiAbelianAwayOfCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExtendsToSemiAbelianAwayOfCharts.lean#L32)), Steps 2 to 6 are `GlobalTheory.SymDiv.exists_ampleDiv_symm`, `GlobalTheory.Desc.chart_part`, `exists_cartierDiv_closure`, `ampleDiv_closure_on_chart` and `GlobalTheory.Desc.hasExt_of_setup`; the charts are chosen by `(hC x).some` at line 38, so the setup depends on a choice. In the theorem on extension over an affine open ([ExistsSemiAbelianExtensionNearPoint.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsSemiAbelianExtensionNearPoint.lean#L111)), Step 3 is `GlobalTheory.Desc.Chart.nonempty_restrict` and Step 5 is `GlobalTheory.Desc.HasExt.of_dense` with `GlobalTheory.Desc.HasExt.of_comp`; only the charts at points of $U$ are used. The published theorem is the statement `SemiAbelianHomExtension`; we did not unfold its proof, and the reference to Faltings and Chai is ours. In the last theorem ([SemiAbelianDescentFromCompleteRegularCharts.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SemiAbelianDescentFromCompleteRegularCharts.lean#L14)), Steps 2 and 3 are `GlobalTheory.T.extendsToSemiAbelian_of_locally_normal_noetherian` and `GlobalTheory.T.exists_grpPullback_completionChart_to_extension`. We did not open the proofs of these inputs, and the reasons given for Steps 2 and 3 of the last theorem and for the inputs of the first are sketches. Condition 2 of a chart is `IsEtaleCompletion` with the field `unr`, and normality of $S$ is `IsNormalScheme`.
