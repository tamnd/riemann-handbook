---
title: Kleiman intersection numbers on multiprojective models
decls:
  - PositivityTheory.HtPt.Ktw.a14
  - PositivityTheory.HtPt.Ktw.a15
  - PositivityTheory.HtPt.Ktw.a16
  - PositivityTheory.HtPt.Ktw.a17
  - PositivityTheory.HtPt.Ktw.a18
  - PositivityTheory.HtPt.Ktw.a27
  - PositivityTheory.HtPt.Ktw.k_twins
  - PositivityTheory.HtPt.Kra.kleiman_input
  - PositivityTheory.HtPt.Kra.kleiman_input_universe_zero
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Kleiman intersection numbers on multiprojective models

This last section proves the facts on intersection numbers and positivity that the rest of the proof uses: Kleiman's theorem that nef classes have nonnegative products, the multiprojective form of "nef plus ample is ample", and a lower bound for the number of sections. Intersection numbers are defined by the method of Snapper and Kleiman, from the dimensions of spaces of sections of large twists. The main work is to compute them on a model of a projective variety in a product of projective spaces, through Čech cohomology and Serre vanishing ([coherent cohomology](/learn/commutative-algebra/#coherent-cohomology)). The results are used in [the literature step](/step/every-character-of-literature/).

### Models with a base block

Let $F \subseteq \Omega$ be fields, $K$ a finite set and $\iota_k$ a finite set for each $k \in K$. A point $y = (y_{k,i})$ with entries in $\Omega$ gives the prime $V \subset F[x_{k,i}]$, the kernel of $x_{k,i} \mapsto y_{k,i} t_k$ into $\Omega[t_k : k \in K]$. It is the multihomogeneous ideal of the subvariety of $\prod_k \mathbb{P}^{\iota_k}$ with generic point $y$. For $m \in \mathbb{Z}^K$ let $h_V(m)$ be the dimension of the part of degree $m$ of $F[x]/V$, and let $\Gamma(m) \subseteq \Omega$ be the space of sections of $\mathcal{O}(m)$ on $V$: the $s$ with $s \prod_k y_{k,c_k}^{-m_k}$ in the chart ring $F[y_{k,i}/y_{k,c_k}]$ for each chart $c$ with $y_{k,c_k} \neq 0$.

**Definition 7.12.1 (Model with a base block).** Fix $k_0 \in K$, let $x = y_{k_0} \in \Omega^{N+1}$, and let $X \subseteq \mathbb{P}^N$ be the closure of $x$. The point $y$ is a *model with base block* $k_0$ if each block of $y$ has a nonzero entry and the charts of $V$ and of $X$ give the same local rings in $\Omega$. Then the projection $V \to X$ is an isomorphism. Let $e_{k_0} \in \mathbb{Z}^K$ be the unit vector at $k_0$; the bundle $\mathcal{O}(e_{k_0})$ on $V$ is $\mathcal{O}_X(1)$.

A *cell* of $V$ is the open set where $y_{k,c_k} \neq 0$ for all $k$, for a chart $c$. Let $\check H^i(m)$ be the Čech cohomology in degree $m$ of the graded module $F[x]/V$ for the cover of $V$ by its cells, with linear orders fixed on $K$ and on each $\iota_k$.

**Theorem 7.12.2 (Exactness over a base chart).** Let $y$ be a model with base block $k_0$, $\gamma \in \mathbb{Z}^K$, and $J$ a standard chart of $X$. Then the Čech complex of the cells of $V$ that lie over $J$, in degree $\gamma$ and augmented by the sections of degree $\gamma$ over $J$, is exact.

Lean: `PositivityTheory.HtPt.Ktw.a14`.

*Proof sketch.* The chart $X_J$ is affine, and since $y$ is a model it is also the part of $V$ over $J$. The cells over $J$ form a finite cover of it by open affines. The augmented Čech complex of a quasi-coherent sheaf for such a cover of an affine scheme is exact (Hartshorne, Chapter III, §4). The formal proof assembles this from seven lemmas on the cell rings, with a contracting homotopy for the cell complex. $\square$

**Theorem 7.12.3 (Chart cohomology is cell cohomology).** Let $y$ be a model with base block $k_0$ and $\gamma \in \mathbb{Z}^K$. Let $T$ be a system of modules on the standard charts of $X$ whose module on each chart $J$ is the space of sections of degree $\gamma$ over $J$. Then for each $n$ the Čech cohomology $H^n(X, T)$ for the standard cover of $X$ is isomorphic to $\check H^n(\gamma)$.

Lean: `PositivityTheory.HtPt.Ktw.a15`.

*Proof sketch.* Compare both sides with the double Čech complex of the cover of $X$ by charts and the cover of $V$ by cells. By the last theorem, the complexes in the cell direction are exact after augmentation, so the total complex computes $H^n(X, T)$. Since the cells refine the charts, a contraction in the chart direction shows that it also computes $\check H^n(\gamma)$. $\square$

**Theorem 7.12.4 (Serre vanishing along the base direction).** Let $y$ be a model with base block $k_0$. For each $\beta \in \mathbb{Z}^K$ there is $c_0$ with $\check H^i(\beta + c\,e_{k_0}) = 0$ for all $c \geq c_0$ and $i \geq 1$.

Lean: `PositivityTheory.HtPt.Ktw.a16`.

*Proof.* There is a line bundle $Q$ on $X$ with $H^0(X, Q(c)) = \Gamma(\beta + c\,e_{k_0})$ for all $c \in \mathbb{Z}$. By Serre vanishing on $X \subseteq \mathbb{P}^N$ (Hartshorne, Theorem III.5.2) there is $c_0$ with $H^i(X, Q(c)) = 0$ for $i \geq 1$ and $c \geq c_0$. The cohomology of the cells of $V$ is the cohomology of the charts of $X$, by the last theorem, so $\check H^i(\beta + c\,e_{k_0}) \cong H^i(X, Q(c))$. $\square$

**Theorem 7.12.5 (Sections follow the Hilbert polynomial).** Let $y$ be a model with base block $k_0$. There is a polynomial $P \in \mathbb{Q}[t_k : k \in K]$ such that:

1. $h_V(m) = P(m)$ for all $m$ large in every coordinate;
2. for each $\beta \in \mathbb{Z}^K$, $\dim_F \Gamma(\beta + c\,e_{k_0}) = P(\beta + c\,e_{k_0})$ for all large $c$.

Lean: `PositivityTheory.HtPt.Ktw.a17`.

*Proof.* Each $\check H^i(m)$ has finite dimension, the groups vanish for large $i$, and the Euler characteristic $\chi(m) = \sum_i (-1)^i \dim_F \check H^i(m)$ is a polynomial $P$ on all of $\mathbb{Z}^K$. Also $\check H^0(m) \cong \Gamma(m)$. So $\dim \Gamma(m) = P(m)$ at each $m$ where the higher groups vanish. For $m$ large in every coordinate they vanish and $\dim \check H^0(m) = h_V(m)$, which gives 1 ([the Hilbert polynomial](/learn/commutative-algebra/#coherent-cohomology), Hartshorne, Theorem I.7.5). Along the ray $\beta + c\,e_{k_0}$ they vanish by the last theorem, which gives 2. $\square$

### Intersection numbers

**Definition 7.12.6 (Intersection number).** Let $X \subseteq \mathbb{P}^N$ be a subvariety of dimension $n$, and $L_1, \dots, L_n$ line bundles on $X$, given by invertible modules on the charts. The *intersection number* is
$$(L_1 \cdots L_n)_X = \lim_{c \to \infty} \sum_{T \subseteq \{1, \dots, n\}} (-1)^{n - |T|} \dim_F H^0\Bigl(X, \textstyle\bigotimes_{i \in T} L_i \otimes \mathcal{O}(c)\Bigr).$$
For a multiprojective prime $W$ of relative dimension $n$ and $\delta_1, \dots, \delta_n \in \mathbb{Z}^K$, the *mixed multidegree* $\deg_W(\delta_1, \dots, \delta_n)$ is the eventual value of $\Delta_{\delta_1} \cdots \Delta_{\delta_n} h_W(m)$, where $\Delta_b h(m) = h(m) - h(m - b)$ and "eventual" means for $m$ large in every coordinate.

For large $c$ the twisted bundles have no higher cohomology, so the sum is the mixed difference of the Euler characteristic of Snapper and Kleiman.

**Theorem 7.12.7 (Intersection numbers from a model).** Let $y$ be a model with base block $k_0$, with $X$ of dimension $n$. Let $L_1, \dots, L_n$ be line bundles on $X$ and $\delta_1, \dots, \delta_n \in \mathbb{Z}^K$ with $H^0(X, L_i(c)) = \Gamma(\delta_i + c\,e_{k_0})$ for all $c \in \mathbb{Z}$. Then $(L_1 \cdots L_n)_X = \deg_V(\delta_1, \dots, \delta_n)$.

Lean: `PositivityTheory.HtPt.Ktw.a18`.

*Proof.* Since $X$ has dimension $n$, $V$ has relative dimension $n$, and $\Delta_{\delta_1} \cdots \Delta_{\delta_n} h_V$ is eventually a constant $D$. Let $P$ be the polynomial of the last theorem. Its mixed difference is a polynomial that equals $D$ on a product of infinite sets, so it is $D$ everywhere. For large $c$ we have $H^0(X, \bigotimes_{i \in T} L_i(c)) = \Gamma(\sum_{i \in T} \delta_i + c\,e_{k_0})$, of dimension $P(\sum_{i \in T} \delta_i + c\,e_{k_0})$. So the sum in the definition is the mixed difference of $P$ at $\sum_i \delta_i + c\,e_{k_0}$, which is $D$. $\square$

A class $\beta \in \mathbb{Z}^K$ is *nef* on $y$ if $\deg_W(\beta) \geq 0$ for every multiprojective prime $W \supseteq V$ of relative dimension $1$, that is, on every curve of $V$.

**Theorem 7.12.8 (Nefness does not depend on the model).** Let $y$ and $y'$ be models with base blocks $k_0$ and $k_0'$ and the same base vector $x$. Let $\beta, \beta'$ be classes with $\Gamma_y(\beta + c\,e_{k_0}) = \Gamma_{y'}(\beta' + c\,e_{k_0'})$ for all $c \in \mathbb{Z}$. Then $\beta$ is nef on $y$ if and only if $\beta'$ is nef on $y'$.

Lean: `PositivityTheory.HtPt.Ktw.a27`.

*Proof.* Subvarieties of $V$ of dimension $d$ map onto subvarieties of $X$ of dimension $d$, and each subvariety of $X$ of dimension $d$ is such an image. So each curve $W$ of $V$ has a curve $W'$ of $V'$ with the same image in $X$, and conversely. By the last theorem, applied on $W$ and $W'$, both degrees $\deg_W(\beta)$ and $\deg_{W'}(\beta')$ are the degree of the same line bundle on the image curve. $\square$

**Theorem 7.12.9 (Rules for intersection numbers).** For each field $k$ and each subvariety of $\mathbb{P}^N_k$ with generic point in a field $\Omega$, the intersection number of the definition satisfies the following.

1. The sum in the definition is eventually constant in $c$.
2. It does not change when the $L_i$ are permuted.
3. It is additive in each $L_i$.
4. If $s$ is a section of $L_n$ that does not vanish on $X$, then $(L_1 \cdots L_n)_X = \sum_{Z} m_Z(s)\, (L_1 \cdots L_{n-1})_Z$, over the components $Z$ of $X \cap \{s = 0\}$ of dimension $n - 1$, with multiplicities $m_Z(s)$.
5. For $n = 0$ it is the degree of the residue field of the point over $k$.

Lean: `PositivityTheory.HtPt.Kra.kleiman_input` (also `PositivityTheory.HtPt.Kra.kleiman_input_universe_zero`, its case of universe $0$).

*Proof sketch.* Rules 1, 3, 4 and 5 are four lemmas, and rule 2 holds since the sum over $T$ is symmetric. Rule 4 is derived from a shift formula for mixed twists. Classically it comes from the exact sequence $0 \to L_n^{-1} \to \mathcal{O}_X \to \mathcal{O}_{\{s = 0\}} \to 0$: tensored with the other bundles, it turns the mixed difference over $X$ into the mixed difference over the divisor of $s$. $\square$

**Theorem 7.12.10 (Kleiman's positivity facts).** Assume the rules of the last theorem. Let $y$ be a point of $\prod_k \mathbb{P}^{\iota_k}$.

1. If $\mu_1, \dots, \mu_d$ are nef and $V$ has relative dimension $d$, then $\deg_V(\mu_1, \dots, \mu_d) \geq 0$.
2. If $y$ is a model with base block $k_0$, $\mu$ is nef and $t > 0$ is rational, then there are $a \geq 1$ and $m = a t$ such that $a \mu + m\, e_{k_0}$ is very ample.
3. If $y$ is a model with base block $k_0$ of relative dimension $d + 1$, $\nu$ is very ample and $q \geq 1$, then there is $C$ with
$$\bigl(\deg_V(\nu^{d+1}) - (d+1) \deg_V(\nu^{d} \cdot q\,e_{k_0})\bigr) \frac{n^{d+1}}{(d+1)!} - C n^d \leq \dim_F \Gamma\bigl(n(\nu - q\,e_{k_0})\bigr) \quad (n \geq 1).$$

Lean: `PositivityTheory.HtPt.Ktw.k_twins`.

*Proof sketch.* Each part is first proved in one projective space, from the five rules. Part 1 is Kleiman's theorem (Lazarsfeld, Theorem 1.4.9). Part 2 is the statement that nef plus ample is ample, and part 3 has the form of Siu's inequality, a lower bound for the sections of a difference of two nef classes. Each statement then moves to the product of projective spaces. The Segre embedding realizes the multiprojective data in one projective space. The theorems on models of this section, intersection numbers from a model and the independence of nefness, compare the two sides. $\square$

Part 3 gives nonzero sections of $n(\nu - q\,e_{k_0})$ for large $n$ when the leading coefficient is positive.

**Remark 7.12.11 (Formalization).** The theorems `a14` to `a18` are in [A12.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/A12.lean#L103), lines 103, 114, 120, 125 and 130, `a27` is in [A28.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/A28.lean#L68), line 68, and `k_twins` is in [KTwins.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/KTwins.lean#L40). Each composes lemmas of the folder `KleimanAmpleness`, whose statements we read; the proofs above follow that composition. The intersection number is `interNum` and the sum is `interSum`, in [AlgebraMapMemChartRingLine.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/AlgebraMapMemChartRingLine.lean#L89). `interNum` is `limUnder atTop`, which takes a default value when the sequence has no limit; rule 1 is the statement that it has one. The rules are the hypothesis `GenericPointSectionInput.Statement` in [GenericPointSectionHypotheses.lean](lean:GroundTheory/HeightsAndTheta/Heights/KleimanAmpleness/GenericPointSectionHypotheses.lean#L202), and `kleiman_input` in [KleimanInputUniverseZero.lean](lean:Development/WeilBound/CoreStatements/HodgeTatePoints/KleimanInputUniverseZero.lean#L14) proves it from `interNumEventual`, `interNumAdditive`, `intersectionNumberCut_of_mixedTwistShift` and `interNumPointDeg`. The theorem `kleiman_input_universe_zero` (line 18) is `kleiman_input` at universes $0$, the form that `k_twins` takes as hypothesis. The Segre transfer in part 1 is `unfolding_matrix_of_form` in KleimanNefF.lean, line 42, a name that does not describe it. The names `a14` to `a27`, the folder `HodgeTatePoints` and the namespace `IndefiniteRowSideFullHecke.Kleiman2` of the statements do not describe the content: no Hodge-Tate weight or Hecke operator appears.

## Notes and references

The chapter feeds four parts of the proof. Sections 1 to 7 compute the Chern integrals of the Hodge metric, show that the metric is good at the boundary, and prove Mumford's proportionality theorem; the result is used through [the classical theorems](/entry/to-classical-theorems/) by the field `p16` of [the published results](/step/published-results-arithmetic/). Section 8 gives the freeness of Hodge modules used in [freeness at component stalks](/entry/hfree-at-component-stalks/). Section 9 gives the finite parts and test orders of [the ordinary curve relay](/entry/relay-ordinary-curve-model-relay/) and [the Hodge relay for arithmetic varieties](/entry/relay-arith-variety-model-hodge-relay/). Sections 10 and 11 give inputs of [the covolume bound](/entry/top-covol-slim2-use-alt-alt/), [the blow-up fibre theorem](/entry/blow-up-fibre-main/) and [the deep slim theorem](/entry/deep-slim-use/). Section 12 gives the positivity facts of [the literature step](/step/every-character-of-literature/).

- D. Mumford, Hirzebruch's proportionality theorem in the non-compact case, Invent. Math. 42 (1977), 239 to 272, for Sections 1 to 7.
- W. Schmid, Variation of Hodge structure: the singularities of the period mapping, Invent. Math. 22 (1973), 211 to 319, for the growth estimates of Sections 5 and 6.
- G. Faltings and C.-L. Chai, *Degeneration of Abelian Varieties*, Ergeb. Math. Grenzgeb. (3) 22, Springer, 1990, Chapters III and IV, for Mumford's construction and toroidal compactifications, used in Sections 5, 7 and 9.
- P. Griffiths and J. Harris, *Principles of Algebraic Geometry*, Wiley, 1978, Chapter 0, §5, and Chapter 1, §5, for Chern forms and Grassmannians in Sections 1 to 3.
- J. Milnor and J. Stasheff, *Characteristic Classes*, Ann. of Math. Stud. 76, Princeton Univ. Press, 1974, §14, for Chern classes in Section 1.
- D. Mumford, *Abelian Varieties*, Oxford Univ. Press, 1970, §6 and §10, for the theorem of the cube used in Section 10, and §12, Theorem 1, for the quotients of Section 11.
- Yu. G. Zarhin, A remark on endomorphisms of abelian varieties over function fields of finite characteristic, Math. USSR-Izv. 8 (1974), 477 to 480, for Zarhin's trick in Section 11.
- H. Hironaka, Resolution of singularities of an algebraic variety over a field of characteristic zero I, II, Ann. of Math. 79 (1964), 109 to 203 and 205 to 326, for the hypotheses of Section 11.
- J.-B. Bost, H. Gillet and C. Soulé, Heights of projective varieties and positive Green forms, J. Amer. Math. Soc. 7 (1994), 903 to 1027, for heights defined by the recursion of Section 11.
- W. Fulton, *Intersection Theory*, Ergeb. Math. Grenzgeb. (3) 2, Springer, 1984, Chapter 1 and Appendix A, for multiplicities and lengths in Sections 11 and 12.
- S. Kleiman, Toward a numerical theory of ampleness, Ann. of Math. 84 (1966), 293 to 344, for the intersection numbers of Section 12.
- R. Lazarsfeld, *Positivity in Algebraic Geometry I*, Ergeb. Math. Grenzgeb. (3) 48, Springer, 2004, Theorem 1.4.9, Corollary 1.4.10 and §2.2, for the three parts of Kleiman's positivity facts.
- R. Hartshorne, *Algebraic Geometry*, Grad. Texts in Math. 52, Springer, 1977, Chapter I, §7, for Hilbert polynomials, and Chapter III, §4 and Theorem III.5.2, for Čech cohomology and Serre vanishing in Section 12.
