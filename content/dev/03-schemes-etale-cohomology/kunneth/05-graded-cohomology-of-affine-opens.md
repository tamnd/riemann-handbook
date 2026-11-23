---
title: Graded cohomology of affine opens
decls:
  - GlobalTheory.T.affine_graded_cohomology_vanishing
  - GlobalTheory.CompanionTheory.GrForm.gr_aff
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Graded cohomology of affine opens

On a smooth affine scheme over a field of characteristic $0$, the graded pieces of the divided power filtration on the thickening site have cohomology in one degree only. This is the analogue, on the thickening site, of the vanishing of $H^j(V, \Omega^r)$ for $j > 0$ on an affine $V$, together with the identification of the graded piece of degree $r$ with $\Omega^r$ placed in degree $r$. We prove the vanishing from a local computation on opens with coordinates and a Čech spectral sequence argument. The result is [the vanishing on affine opens](/entry/gr-aff-pf/) of the comparison chapter. There it is one of the inputs of the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).

We use the site of thickenings and the graded pieces of [the chapter on the $\ell$-adic Hodge comparison](/entry/hodge-affine-iso-sign/). Let $K$ be a field and $q : X \to \operatorname{Spec} K$ a [[smooth|EXKGG9X6J0]] scheme. A thickening of an open $W \subseteq X$ is, roughly, a $K$-algebra $B$ with a divided power ideal $J$ and a point of $W$ with values in $B/J$. The functor $T \mapsto B$ has the divided power filtration $J^{[r]}$.

**Definition 1.5.1 (Truncated thickening sites).** Let $s \geq 1$ and let $\mathcal{V}$ be a set of opens of $X$. Let $\mathcal{T}_s(\mathcal{V})$ be the full subcategory of thickenings $T$ with $J^{[s]} = 0$ whose point lies in some $W \in \mathcal{V}$. For $r < s$ write
$$H^j\bigl(\mathcal{T}_s(\mathcal{V}), \operatorname{gr}^r\bigr) = H^j\bigl(\mathcal{T}_s(\mathcal{V}), J^{[r]} / J^{[r+1]}\bigr)$$
for the cohomology of the graded piece on this category, computed by the nerve complex of the functor.

For $\mathcal{V} = \{V\}$ we write $\mathcal{T}_s(V)$. The truncation $J^{[s]} = 0$ makes the filtration finite, so only $r < s$ is of interest.

The theorem is proved under five general statements about the thickening site. We list them first. A *frame* is an open with coordinates $t_1, \dots, t_d$ together with the polynomial model of its thickenings that these coordinates give.

- (H1) *Local graded computation.* On a frame of dimension $d$, if the graded pieces of the base are constant and the polynomial model satisfies the critical condition in all degrees $r' \leq r + 1$, then $H^j(\operatorname{gr}^r) = 0$ for $r < j$. When $r = j + p$, each class of degree $j$ is represented by a form $\sum_{|I| = j} x_I \, dt_I$ with $x_I \in \operatorname{Fil}^p$ of the base, and a form that represents $0$ has all $x_I \in \operatorname{Fil}^{p+1}$.
- (H2) *Local vanishing.* On a frame of dimension $d$, if two families of ideals $a_{r'} \subseteq b_{r'}$ satisfy a ladder condition and the inclusion holds on the frame for $r - d \leq r' \leq r$, then all cohomology of the quotient $b_r / a_r$ vanishes.
- (H3) *Polynomial models.* For every $s$ and every set of opens $\mathcal{V}$, the site $\mathcal{T}_s(\mathcal{V})$ has a polynomial model that satisfies the critical condition for the divided power filtration and the standard ideals in all degrees $r \leq s$.
- (H4) *Serre classes.* The statement of Lemma 8.5.4 below.
- (H5) *Global vanishing.* Let $(U_\alpha)_{\alpha \in A}$ be a finite family of opens. If the cohomology over every nonempty finite intersection of the $U_\alpha$ vanishes below degree $s$, or in all degrees, or above degree $s$, then the cohomology over the union vanishes below degree $s$, or in all degrees, or in degrees at least $s + \#A$, respectively.

**Theorem 1.5.2 (Vanishing on affine opens).** Assume (H1) to (H5). Let $K$ be a field of characteristic $0$, $q : X \to \operatorname{Spec} K$ smooth and $V \subseteq X$ an affine open. Let $s, r, j \geq 0$ with $r < s$ and $j \neq r$. Then
$$H^j\bigl(\mathcal{T}_s(V), \operatorname{gr}^r\bigr) = 0.$$

Lean: `GlobalTheory.T.affine_graded_cohomology_vanishing` (also `GlobalTheory.CompanionTheory.GrForm.gr_aff`, the same statement).

The classical analogue is Serre's theorem: a quasi-coherent sheaf on an affine scheme has no higher cohomology (R. Hartshorne, *Algebraic Geometry*, Chapter III, Theorem 3.5). On the thickening site the graded piece of degree $r$ behaves like $\Omega^r$ placed in degree $r$, so its cohomology on an affine open sits in degree $r$ alone. The proof uses (H1), (H3) and (H4). It does not use (H2) and (H5).

**Definition 1.5.3 (Coordinate open).** An open $W \subseteq X$ has *coordinates* if $W$ is affine and there are $t_1, \dots, t_d \in \mathcal{O}(W)$ with $K[t_1, \dots, t_d] \to \mathcal{O}(W)$ étale.

**Lemma 1.5.4 (Čech spectral sequence and Serre classes).** Let $F$ be a functor on the thickening site with values in modules, $Q$ a condition on thickenings, $(U_\alpha)$ a family of opens, and $\mathcal{S}$ a Serre class of modules. Let $n \geq 0$. If for all $a + b = n$ the Čech cohomology $\check H^a$ of the presheaf $W \mapsto H^b(Q(W), F)$ on the family lies in $\mathcal{S}$, then $H^n$ of $F$ on the thickenings over the union lies in $\mathcal{S}$.

Lean: `CrystallineSemistableComparison.Pb.KH.GlobSerreSt` (a proposition, used as a hypothesis).

This is the abutment statement of the Čech-to-derived spectral sequence $E_2^{a,b} = \check H^a(H^b) \Rightarrow H^{a+b}$. The abutment $H^n$ has a finite filtration whose graded pieces are subquotients of the $E_2^{a,b}$ with $a + b = n$. A Serre class is closed under subquotients and extensions, so $H^n$ lies in $\mathcal{S}$.

The proof of the theorem uses three facts about smooth schemes over $K$. We state them in the form in which the proof uses them.

**Lemma 1.5.5 (Inputs for the proof).** Let $K$ be a field of characteristic $0$, $q : X \to \operatorname{Spec} K$ smooth and $r < s$.

1. *Covers.* Each affine open $V$ is a finite union of coordinate opens $U_1, \dots, U_N$ such that every intersection $U_{\alpha_0} \cap \dots \cap U_{\alpha_m}$ is affine.
2. *Coordinate opens.* Assume (H1) and (H3). If $W$ has coordinates, then $H^j(\mathcal{T}_s(W), \operatorname{gr}^r) = 0$ for $j \neq r$.
3. *Vector bundle.* Assume (H1) and (H3). For a cover as in 1, the Čech complex of the presheaf $W \mapsto H^r(\mathcal{T}_s(W), \operatorname{gr}^r)$ on the cover is the Čech complex of a vector bundle on $V$, given by transition functions on the $U_\alpha \cap U_\beta$.

Lean: `GlobalTheory.T.graded_form_cover`, `GlobalTheory.T.graded_form_vanish_of_frame`, `GlobalTheory.T.graded_form_vector_bundle`.

Part 1 holds because a smooth morphism is étale locally over affine space: each point of $V$ has an affine neighbourhood $W \subseteq V$ with an étale map to $\mathbb{A}^d_K$, and finitely many of them cover the quasi-compact $V$. Their intersections are affine because $V$ is affine, hence separated. Part 2 comes from (H1). On a coordinate open the polynomial model of (H3) satisfies the critical condition, so (H1) applies. It gives $H^j(\operatorname{gr}^r) = 0$ for $j > r$. For $j < r$ write $r = j + p$ with $p \geq 1$. A class of degree $j$ is a form $\sum_I x_I \, dt_I$ with $x_I \in \operatorname{Fil}^p$ of the base. The base is $K$ with the zero divided power ideal, so $\operatorname{Fil}^p = 0$ for $p \geq 1$, and the class is $0$. Part 3 identifies $H^r(\operatorname{gr}^r)$ on a coordinate open with the free module of $r$-forms in the $dt_I$. A change of coordinates on an overlap changes this basis by a matrix of functions on the overlap, and these matrices satisfy the cocycle condition.

*Proof of the theorem.* Let $V$ be affine, $r < s$ and $j \neq r$.

1. *The base.* Since $s > r \geq 0$ we have $s \geq 1$. The base ring is $K$ with the zero divided power ideal. Its divided power filtration satisfies $J^{[s]} = 0$, and every nonzero integer is a unit in $K$ since $K$ has characteristic $0$. These are the conditions that the inputs ask of the base ring.
2. *A cover.* Choose a cover $U_1, \dots, U_N$ of $V$ as in part 1 of Lemma 8.5.5.
3. *Refinement.* A thickening over $V$ has its point in $V$, and $V$ is the union of the $U_\alpha$. So the thickenings over the family $(U_\alpha)$ and the thickenings over $V$ have the same cohomology: restriction gives a bijection $H^j(\mathcal{T}_s(V), \operatorname{gr}^r) \to H^j(\mathcal{T}_s(\{U_1, \dots, U_N\}), \operatorname{gr}^r)$. It is enough to show that the right side is $0$.
4. *The $E_2$ terms.* Let $a + b = j$ and consider $\check H^a$ of the presheaf $W \mapsto H^b(\mathcal{T}_s(W), \operatorname{gr}^r)$ on the cover.
   - If $b \neq r$, each intersection of the cover is affine, and it has coordinates, since it is an open of some $U_\alpha$ and the coordinates of $U_\alpha$ restrict to it. So $H^b = 0$ there by part 2 of Lemma 8.5.5, and the Čech complex is $0$.
   - If $b = r$ and $a \geq 1$, the Čech complex is the Čech complex of a vector bundle on the affine $V$ by part 3 of Lemma 8.5.5. Its cohomology in degree $a \geq 1$ is $0$, by Serre's vanishing theorem and the comparison of Čech and sheaf cohomology for an affine cover of a separated scheme (R. Hartshorne, *Algebraic Geometry*, Chapter III, Theorems 3.5 and 4.5).
   - If $b = r$ and $a = 0$, then $j = r$, which is excluded.
5. *Conclusion.* All terms of total degree $j$ are $0$. Lemma 8.5.4, which is (H4), applied with the Serre class of zero modules, gives $H^j(\mathcal{T}_s(\{U_1, \dots, U_N\}), \operatorname{gr}^r) = 0$. By step 3, $H^j(\mathcal{T}_s(V), \operatorname{gr}^r) = 0$. $\square$

**Remark 1.5.6.** Characteristic $0$ enters only in step 1, where an integer $n \neq 0$ must be invertible in $K$. The truncation level $s$ enters only through $r < s$ and $s \geq 1$.

**Remark 1.5.7 (Formalization).** The five statements (H1) to (H5) are hypotheses of the formal theorem. They are proved elsewhere and supplied by the result that uses the theorem. The hypotheses (H2) and (H5) are not used in the proof ([AffineGradedCohomologyVanishing.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AffineGradedCohomologyVanishing.lean#L148)). Our description of (H1) to (H5) follows their formal statements. We have not unfolded the notions of frame, polynomial model and critical condition on which they rest. The three parts of Lemma 8.5.5 are separate formal results. Their statements were checked, and the arguments given for them here are ours. The refinement bijection of step 3 and the vanishing of Čech cohomology of a vector bundle in step 4 are also separate formal results.
