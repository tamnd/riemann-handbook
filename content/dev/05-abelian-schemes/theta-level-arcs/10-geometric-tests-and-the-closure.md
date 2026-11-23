---
title: Geometric tests and the closure
decls:
  - GlobalTheory.T.hasGeometricTest_of_hasUniformisedTest
  - GlobalTheory.ZH.GeoExist.hasGeo_of_hasU
  - GlobalTheory.ZH.baseFacts_hasGeo_exists_clos
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Geometric tests and the closure

Let $S$ be a theta system with a realisation $\rho$ by an abelian scheme $A$ over $\operatorname{Spec} R$, and let $Z$ be a normal projective model of the function field $\Omega$ of $R$. The extension of $A$ over $Z$ starts from local information at $p$-adic points. In this section we turn uniformised tests into geometric tests, which compare the theta coordinates of $A$ with sections of a model with series, and we collect the set-up of the extension: facts on the base, the geometric tests, and a projective closure of $A$ over $Z$ with four properties of its $p$-adic points. The result is the first step of [the extension of a theta-level abelian scheme](/entry/zh-geo/). We keep the notation of [the previous section](/entry/utest-nonempty-mod/).

### Tests

Let $p$ be a prime and let $y_0 : R \to \overline{\mathbb{Q}}_p$ be integral on $o$, that is, $|y_0(a)| \leq 1$ for $a \in o$.

**Definition 6.10.1 (Test).** A *test* $\tau$ of $S$ at $(p, y_0)$ consists of a free abelian group $\mathsf{X}$ of finite rank with a positive real quadratic form $q$, a surjection $\Gamma \to \mathsf{X}/rN\mathsf{X}$ whose kernel $H$ has an orthogonal that is isotropic and free over $\mathbb{Z}/rN$, weights $\mathsf{X} \to \operatorname{Hom}(H^\perp, \mathbb{Z}/N)$ given by the Weil pairing, and the largest value $\delta > 0$ of $|y_0(\vartheta(x))|$, such that: the $x$ with $|y_0(\vartheta(x))| = \delta$ generate $H$; each nonzero value is bounded by $\delta \exp(-q(w)/(rN)^2)$ for a representative $w$ of the class of $x$; and the projections of the values $\operatorname{ev}$ onto the weight spaces have sizes bounded by $\delta \exp(-q(\alpha)/N)$ for shortest $\alpha$, with equality for some entry and with value $\delta$ at weight $0$.

Lean: `GlobalTheory.ZH.ThetaSys.Test`.

The *test lattice* $E_\tau \subset \overline{\mathbb{Q}}_p^J$ is the $\mathcal{O}_p$-span of the vectors $l \cdot y_0(\pi_\alpha)_{\cdot, i}$, where $\alpha$ is a shortest vector for $q$ modulo $N$, $|l| \leq \exp(q(\alpha)/N)$, $\pi_\alpha$ is the projection of $o^J$ onto the weight space of the weight of $\alpha$, and $i \in J$. The system $S$ *has tests* if every $y_0$ integral on $o$ has a test.

A labelling $l$ of a uniformised test $u$ *matches* a test $\tau$ if there is an isomorphism of the lattices that carries the form of $\tau$ to $q$ and the classes of $\tau$ to the classes of $l$.

A matrix $b \in \operatorname{GL}_J(\operatorname{Frac} V)$ *links* the coordinates of $\rho$ to a family $\sigma$ of sections of $H_N$ if, for every point $a$ of the generic fibre of $G$ over $\overline{\mathbb{Q}}_p$ and every vector $v$ of theta coordinates of the image of $a$ in $A$, the vector $b v$ is a vector of coordinates of $a$ for $\sigma$.

**Definition 6.10.2 (Uniformised and geometric tests).** The realisation $\rho$ *has uniformised tests* if, for each prime $p$, each $y_0$ integral on $o$ and each finite set $F_s \subset \overline{\mathbb{Q}}_p$, there are a uniformised test $u$ at $(p, y_0)$ whose field $\operatorname{Frac} V$ contains $F_s$, a labelling $l$ of $u$ and a test $\tau$ that $l$ matches. It *has geometric tests* if, for the same data, there are in addition an adapted family $\sigma$ with classes $\mathrm{cls}$, a model with series for $(u, \sigma)$, and a linking matrix $b$ such that $E_\tau$ is the $\mathcal{O}_p$-span of the rows of $b$ and each row $b_i$ is fixed by the projection onto the weight space of $\mathrm{cls}(i)$.

Lean: `GlobalTheory.ZH.ThetaSys.Real.HasU` (also `GlobalTheory.ZH.ThetaSys.Real.HasGeo`, geometric tests).

The system $S$ is *big* if $N > 1 + 2g\,2^{g/2}$ and $rN$ is larger than two explicit multiples of $N^g g!$, namely $6 N^g g!$ and $2 N^{g+1} g!\, g (3/2)^g 2^{g/2 - 1}$.

### Inputs on geometric tests

These inputs assume the five bundles of laws. They are proved elsewhere in the Lean development.

**Theorem 6.10.3 (Adapted bases exist).** For a labelling $l$ of $u$, $k \geq 1$, and a finite set $J$ with $|J| = k^g$, there is an adapted basis $(\sigma, \mathrm{cls}, f)$ of level $k$ indexed by $J$.

Lean: `GlobalTheory.T.exists_adapted_basis_sections_mod_k`.

**Theorem 6.10.4 (A link matrix).** For an adapted basis $\sigma$ of level $N$, there is a matrix $b$ over $\operatorname{Frac} V$ with $\det b \neq 0$ that links the coordinates of $\rho$ to $\sigma$.

Lean: `GlobalTheory.T.exists_invertible_adaptedBasis_link_matrix`.

**Theorem 6.10.5 (Test lattice).** Let $S$ be big, $y_0$ integral on $o$, $l$ a labelling that matches a test $\tau$, $\sigma$ a family with a model with series, and $b$ an invertible link matrix. Then there is $c \neq 0$ in $\operatorname{Frac} V$ such that $E_\tau$ is the $\mathcal{O}_p$-span of the rows of $cb$.

Lean: `GlobalTheory.T.testLattice_eq_span_model_sections`.

**Theorem 6.10.6 (Weights of the rows).** Assume also the torsion statement for uniformisations. If $\sigma$ is an adapted basis of level $N$ and $b$ links the coordinates of $\rho$ to $\sigma$, then each row $b_i$ is fixed by the projection onto the weight space of $\mathrm{cls}(i)$.

Lean: `GlobalTheory.T.adaptedBasis_rows_have_class_weight`.

### Geometric tests from uniformised tests

**Lemma 6.10.7 (Scaling a link).** If $b$ links the coordinates of $\rho$ to $\sigma$ and $c \neq 0$, then $cb$ also links them.

Lean: `GlobalTheory.ZH.GeoExist.link_smul`.

*Proof.* Coordinates are defined up to a common unit. If $bv$ is a vector of coordinates of $a$ for $\sigma$, so is $c \cdot bv = (cb)v$, since the image of $c$ in $\overline{\mathbb{Q}}_p$ is a unit. $\square$

**Theorem 6.10.8 (Geometric tests).** Assume the five bundles of laws and the torsion statement for uniformisations. Let $o \subset \Omega$ be an arithmetic base and let $S$ be a big theta system with a realisation $\rho$. If $\rho$ has uniformised tests, then $\rho$ has geometric tests.

Lean: `GlobalTheory.T.hasGeometricTest_of_hasUniformisedTest` (also `GlobalTheory.ZH.GeoExist.hasGeo_of_hasU`, a second name).

*Proof.* Fix $p$, $y_0$ integral on $o$ and $F_s$. The uniformised tests give $u$, $l$ and a test $\tau$ that $l$ matches, with $F_s$ in $\operatorname{Frac} V$. Since $N \geq 2$ and the realisation has $|J| = N^g$, there is an adapted basis $(\sigma, \mathrm{cls}, f)$ of level $N$ indexed by $J$. By the theorem that [uniformised tests are models with series](/entry/utest-nonempty-mod/), $(u, \sigma)$ has a model with series. The theorem on a link matrix gives $b$ with $\det b \neq 0$. Since $S$ is big, the theorem on the test lattice gives $c \neq 0$ with $E_\tau$ spanned by the rows of $cb$. By the lemma, $cb$ is a link matrix, and the theorem on weights of the rows applies to it. These data form a geometric test, and $F_s$ lies in $\operatorname{Frac} V$. $\square$

### Models and the closure

**Definition 6.10.9 (Model of the function field).** A *model* $M$ of $\Omega$ over $o$ is an integral scheme $Z$, separated, quasi-compact and locally of finite type over $o$, with a point $\operatorname{Spec} \Omega \to Z$ onto the generic point such that every element of $\Omega$ is a section on some nonempty open set. We write $\mathcal{O}_z \subset \Omega$ for the local ring at $z$. A *lattice system* $E$ assigns to each $z$ an $\mathcal{O}_z$-submodule $E(z) \subset \Omega^J$ that is, near each point, the span of the rows of a fixed invertible matrix.

Lean: `GlobalTheory.ZH.RatModel` (also `GlobalTheory.ZH.RatModel.Lat`, lattice systems).

For $z \in Z$ let $H(z) \subset \Gamma$ be the subgroup generated by the $x$ such that $\vartheta(x) \neq 0$ divides every $\vartheta(x')$ in $\mathcal{O}_z$, and let $T(z) = H(z)^\perp$. An open set $U_0$ is *admissible for $S$* if $Z$ is normal and projective over $o$, every $z$ has such an $x$, $U_0$ is nonempty, $R$ is regular on $U_0$, and the inverses of the nonzero theta values and of certain nonzero theta products are regular on $U_0$. The lattice system $E$ is *fixed by tests* if $E(z)$ is the standard lattice for $z \in U_0$, and, for each $\mathcal{O}_p$-point $y$ of $Z$ centred at $z$ with generic point in $U_0$ and each test $\tau$ at the corresponding $y_0$, the $\mathcal{O}_p$-span of the image of $E(z)$ is $E_\tau$. The Lean names are `GlobalTheory.ZH.ThetaSys.Over₀` and `GlobalTheory.ZH.ThetaSys.IsEE`.

**Definition 6.10.10 (Base facts).** The *base facts* for $(S, M, U_0, E)$ are: admissibility and the condition fixed by tests; $Z$ is a Jacobson space; $H(z)$ is the kernel of the test at each such $p$-adic point; $T(z)$ is isotropic and free with $T(z)^\perp = H(z)$; $T(z) = 0$ on $U_0$; the standard vectors lie in $E(z)$; $E(z)$ is stable under $\rho_S(H(z))$; at closed points the vectors of $E(z)$ of weight $0$ are integral; and ratios of theta values are integral on $E(z)$.

Lean: `GlobalTheory.ZH.BaseFacts`.

**Definition 6.10.11 (Closure).** A *closure* $Q$ of $\rho$ over $(M, U_0, E)$ consists of a map $u_0 : U_0 \to \operatorname{Spec} R$ that is the identity at the generic point; an integral scheme $P$, proper over $Z$ and projective over $o$, that contains $u_0^* A$ as the pullback of $P$ to $U_0$; a line bundle $\mathcal{O}(1)$ on $P$ with sections $(t_i)_{i \in J}$ whose coordinates at points of $u_0^* A$ are the theta coordinates; and an affine cover $(W_\lambda)$ of $Z$ with matrices $B_\lambda$ whose rows span $E(z)$ on $W_\lambda$, and sections over $W_\lambda$ that immerse $P|_{W_\lambda}$ and are related to the $t_i$ by the inverse of $B_\lambda$. The *group part* of $Q$ is the open set $G_Q \subset P$ that is the union, over closed points $z$ and open sets $W$ on which $H(z)$ stays inside the groups $H(z')$, of the parts of $P$ over $W$ where some section of weight $0$ for $T(z)$ does not vanish. An *extension* of $Q$ adds: $Z$ is normal, flat, of finite type and separated over $\mathbb{Z}$, and $U_0$ is nonempty; $u_0^* A$ is an abelian scheme of relative dimension $g$ that maps into $G_Q$; and a section $e$ of $G_Q \to Z$ that extends the zero section.

Lean: `GlobalTheory.ZH.Clos` (also `GlobalTheory.ZH.Clos.Ext`, extensions).

An extension of $Q$ gives a *core* $C$: the data $Z$, $U_0$, $A$, $P$, $G_Q$ and $e$. For an $\mathcal{O}_p$-point $y$ of $Z$ with generic point in $U_0$, a *test of $C$ at $y$* is a complete discrete valuation ring $V$ with a local injection $V \to \mathcal{O}_p$ through which $y$ factors, a smooth separated group scheme $H$ of relative dimension $g$ over $V$ with split special fibre, and a map $H \to G_Q$ over $Z$ that is the identity on generic fibres, a closed immersion on special fibres, and onto the $\mathcal{O}_p$-points over $y$. The four *core properties* are:

1. *tests*: every such $y$ has a test;
2. *independence*: if two such points have the same reduction, each point of $G_Q$ over the first has a point over the second with the same reduction;
3. *fibres*: each point of the special fibre of $G_Q$ over $y$ comes from the special fibre of a test at $y$;
4. *charts*: each point of $Z$ has an immersed neighbourhood with charts of $G_Q$ that split the special fibre of every test at a point over it, with at most $g$ torus coordinates.

Lean: `GlobalTheory.ZJ.Core` (also `GlobalTheory.ZJ.Core.HasCharts`, the fourth property).

### Inputs on the closure

These inputs assume the five bundles of laws, and their proofs are elsewhere in the Lean development.

**Theorem 6.10.12 (Base facts).** If $S$ has tests, $U_0$ is admissible and $E$ is fixed by tests, then the base facts hold.

Lean: `GlobalTheory.ZH.baseFacts_of_isEE`.

**Theorem 6.10.13 (Closure).** If the base facts hold, then $\rho$ has a closure $Q$ over $(M, U_0, E)$, and $Q$ has an extension.

Lean: `GlobalTheory.T.nonempty_abelianSchemeProjectiveClosure` (also `GlobalTheory.T.nonempty_closureExtension_abelianScheme`, the extension).

**Theorem 6.10.14 (Tests and independence).** If the base facts hold, $S$ is big and $\rho$ has geometric tests, then the core of every extension of a closure has tests and independence.

Lean: `GlobalTheory.T.closure_tests_exist_and_reduction_independent`.

**Theorem 6.10.15 (Fibres).** Every core with independence has the fibre property.

Lean: `GlobalTheory.T.fibre_eq_specialFibre_of_reduction_indep`.

**Theorem 6.10.16 (Charts).** If the base facts hold, $S$ is big, $\rho$ has geometric tests and the core has the fibre property, then the core has charts.

Lean: `GlobalTheory.T.hasGradedCharts_near_generic_point_closure`.

### The set-up

**Theorem 6.10.17 (Base facts, geometric tests and a closure).** Assume the five bundles of laws and the torsion statement for uniformisations. Let $S$ be a big theta system over an arithmetic base, with a realisation $\rho$ that has uniformised tests. Let $M$ be a model of $\Omega$, $U_0$ an admissible open set, and $E$ a lattice system fixed by tests. Then the base facts hold, $\rho$ has geometric tests, and there are a closure $Q$ of $\rho$ and an extension of $Q$ whose core has tests, independence, fibres and charts.

Lean: `GlobalTheory.ZH.baseFacts_hasGeo_exists_clos`.

*Proof.* First, $S$ has tests: for $y_0$ integral on $o$, the uniformised tests for $y_0$ and the empty set $F_s$ give a test $\tau$. The theorem on base facts now gives the base facts. The theorem on geometric tests gives geometric tests for $\rho$. The theorem on the closure gives a closure $Q$ and an extension of $Q$. The theorem on tests and independence gives the first two core properties, the theorem on fibres gives the third from independence, and the theorem on charts gives the fourth. $\square$

**Remark 6.10.18 (Formalization).** The geometric tests are built in [HasGeometricTestOfHasUniformisedTest.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTest.lean#L33), with the lemma on scaling at line 21, and the statement form is a `first | exact ...` block in [HasGeometricTestOfHasUniformisedTestStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/HasGeometricTestOfHasUniformisedTestStatement.lean#L14). The set-up is in [BaseFactsHasGeoExistsClos.lean](lean:Development/AbelianVarietyTheory/Proofs/DegenerationProofs/BaseFactsHasGeoExistsClos.lean#L22). The torsion statement for uniformisations is used in the set-up only through the geometric tests, and in the geometric tests only through the models with series and the weights of the rows; bigness is used only for the test lattice and for the closure inputs. In the set-up, the existence of tests of $S$ takes the uniformised test and the matching only to discard them. We did not unfold `S.FF`, `S.proj`, `ImmBy`, `Charts`, `Charts.Split` or the conditions on the theta products in admissibility.
