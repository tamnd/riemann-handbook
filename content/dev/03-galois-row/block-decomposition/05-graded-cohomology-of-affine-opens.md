---
title: Graded cohomology of affine opens
decls:
  - GlobalTheory.T.affine_graded_cohomology_vanishing
  - GlobalTheory.CompanionTheory.GrForm.gr_aff
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Graded cohomology of affine opens

On a smooth affine scheme over a field of characteristic $0$, the graded pieces of the divided power filtration on the thickening site have cohomology in one degree only. This is the analogue, on the thickening site, of the vanishing of $H^j(V, \Omega^r)$ for $j > 0$ on an affine $V$, together with the identification of the graded piece of degree $r$ with $\Omega^r$ placed in degree $r$. The section proves the vanishing statement from a local computation on opens with coordinates and a Čech spectral sequence argument.

We use the site of thickenings and the graded pieces of [the chapter on the $\ell$-adic Hodge comparison](/entry/hodge-affine-iso-sign/). Let $K$ be a field and $q : X \to \operatorname{Spec} K$ a [[smooth|EXKGG9X6J0]] scheme. A thickening of an open $W \subseteq X$ is, roughly, a $K$-algebra $B$ with a divided power ideal $J$ and a point of $W$ with values in $B/J$. The structure functor $T \mapsto B$ has the divided power filtration $J^{[r]}$.

**Definition (Truncated thickening sites).** Let $s \geq 1$ and let $\mathcal{V}$ be a set of opens of $X$. Let $\mathcal{T}_s(\mathcal{V})$ be the full subcategory of thickenings $T$ with $J^{[s]} = 0$ whose point lies in some $W \in \mathcal{V}$. For $r < s$ write
$$H^j\bigl(\mathcal{T}_s(\mathcal{V}), \operatorname{gr}^r\bigr) = H^j\bigl(\mathcal{T}_s(\mathcal{V}), J^{[r]} / J^{[r+1]}\bigr)$$
for the cohomology of the graded piece on this category, computed by the nerve complex of the functor.

For $\mathcal{V} = \{V\}$ we write $\mathcal{T}_s(V)$. The truncation $J^{[s]} = 0$ makes the filtration finite, so only $r < s$ is of interest.

**Theorem (Vanishing on affine opens).** Let $K$ be a field of characteristic $0$, $q : X \to \operatorname{Spec} K$ smooth and $V \subseteq X$ an affine open. Let $r < s$ and $j \neq r$. Then
$$H^j\bigl(\mathcal{T}_s(V), \operatorname{gr}^r\bigr) = 0.$$

Lean: `GlobalTheory.T.affine_graded_cohomology_vanishing` (also `GlobalTheory.CompanionTheory.GrForm.gr_aff`, the same statement).

The classical analogue is Serre's theorem: a quasi-coherent sheaf on an affine scheme has no higher cohomology (R. Hartshorne, *Algebraic Geometry*, Chapter III, Theorem 3.5). On the thickening site the graded piece of degree $r$ behaves like $\Omega^r$ placed in degree $r$, so its cohomology on an affine open sits in degree $r$ alone.

**Remark.** In Lean the theorem is stated under five hypotheses, each a proposition that is proved elsewhere in the code: a local computation of graded pieces on a frame, a local vanishing statement, a transfer statement for polynomial rings, a Serre class statement for the Čech spectral sequence, and a global vanishing statement. Two of them, the local vanishing statement and the global vanishing statement, are not used by the proof ([AffineGradedCohomologyVanishing.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/AffineGradedCohomologyVanishing.lean#L148)). The parent result supplies all five from their proofs in the code.

The proof uses three inputs on the thickening site. We state them in the form in which the proof uses them.

**Definition (Coordinate open).** An open $W \subseteq X$ has *coordinates* if $W$ is affine and there are $t_1, \dots, t_d \in \mathcal{O}(W)$ with $K[t_1, \dots, t_d] \to \mathcal{O}(W)$ étale.

**Lemma (Inputs for the proof).** Let $K$ be a field of characteristic $0$, $q : X \to \operatorname{Spec} K$ smooth and $r < s$.

1. *Covers.* Each affine open $V$ is a finite union of coordinate opens $U_1, \dots, U_N$ such that every intersection $U_{\alpha_0} \cap \dots \cap U_{\alpha_m}$ is affine.
2. *Coordinate opens.* If $W$ has coordinates, then $H^j(\mathcal{T}_s(W), \operatorname{gr}^r) = 0$ for $j \neq r$.
3. *Vector bundle.* For a cover as in 1, the Čech complex of the presheaf $W \mapsto H^r(\mathcal{T}_s(W), \operatorname{gr}^r)$ on the cover is the Čech complex of a vector bundle on $V$, given by transition functions on the $U_\alpha \cap U_\beta$.

Lean: `GlobalTheory.T.graded_form_cover`, `GlobalTheory.T.graded_form_vanish_of_frame`, `GlobalTheory.T.graded_form_vector_bundle`.

Part 2 comes from the local computation on a frame, which shows that on a coordinate open the cohomology of $\operatorname{gr}^r$ in degree $j$ is spanned by forms $\sum_I x_I \, dt_I$ with $|I| = j$ and coefficients $x_I$ in a step of the filtration of the base. Over a field with the zero divided power ideal only the step $0$ survives, so $j = r$. This explanation of part 2 is our reading of the statement of the local computation. Part 3 identifies $H^r(\operatorname{gr}^r)$ on a coordinate open with the free module of $r$-forms in the $dt_I$, which changes by a matrix of functions on overlaps. We have read the statements of these three inputs in the Lean code; we have not unfolded the notions of frame and of polynomial transfer on which their proofs rest.

**Lemma (Čech spectral sequence and Serre classes).** Let $F$ be a functor on the thickening site with values in modules, $Q$ a condition on thickenings, $(U_\alpha)$ a family of opens, and $\mathcal{S}$ a Serre class of modules. Let $n \geq 0$. If for all $a + b = n$ the Čech cohomology $\check H^a$ of the presheaf $W \mapsto H^b(Q(W), F)$ on the family lies in $\mathcal{S}$, then $H^n$ of $F$ on the thickenings over the union lies in $\mathcal{S}$.

Lean: `CrystallineSemistableComparison.Pb.KH.GlobSerreSt` (a proposition, used as a hypothesis).

In words: the Čech-to-derived spectral sequence $E_2^{a,b} = \check H^a(H^b) \Rightarrow H^{a+b}$ has its abutment of degree $n$ in $\mathcal{S}$ when all its terms of total degree $n$ lie in $\mathcal{S}$, since a Serre class is closed under subquotients and extensions. It is a hypothesis of the theorem in Lean, proved elsewhere in the code.

*Proof of the theorem.* Let $V$ be affine, $r < s$ and $j \neq r$.

1. *The base is a lattice base.* Since $s \geq 1$ and $K$ has characteristic $0$, the zero divided power ideal of $K$ satisfies the conditions that the inputs ask of the base ring: $J^{[s]} = 0$, and every nonzero integer is a unit.
2. *A cover.* Choose a cover $U_1, \dots, U_N$ of $V$ as in part 1 of the inputs.
3. *Refinement.* The thickenings over the family $(U_\alpha)$ and the thickenings over $V$ have the same cohomology, since the $U_\alpha$ cover $V$. A refinement lemma of the code gives this bijection.
4. *The $E_1$ terms.* Let $a + b = j$ and consider $\check H^a$ of the presheaf $W \mapsto H^b(\mathcal{T}_s(W), \operatorname{gr}^r)$ on the cover.
   - If $b \neq r$, each intersection of the cover is affine and inherits coordinates from one $U_\alpha$, so $H^b = 0$ there by part 2. The Čech complex is $0$.
   - If $b = r$ and $a \geq 1$, the Čech complex is the Čech complex of a vector bundle on the affine $V$ by part 3. Its cohomology in degree $a \geq 1$ is $0$. This is a lemma of the code; classically it is Serre's vanishing theorem combined with the comparison of Čech and sheaf cohomology (R. Hartshorne, *Algebraic Geometry*, Chapter III, Theorems 3.5 and 4.5).
   - If $b = r$ and $a = 0$, then $j = r$, which is excluded.
5. *Conclusion.* All terms of total degree $j$ are $0$. The lemma on the Čech spectral sequence, applied with the Serre class of zero modules, gives $H^j(\mathcal{T}_s(V), \operatorname{gr}^r) = 0$. $\square$

**Remark.** Characteristic $0$ enters only in step 1, where an integer $n \neq 0$ must be invertible in $K$. The truncation level $s$ enters only through $r < s$ and $s \geq 1$. The Lean proof raises the limit on elaboration steps to $2 \cdot 10^6$ for the main lemma.

The theorem is passed on unchanged as [the vanishing on affine opens](/entry/gr-aff-pf/) of the comparison chapter. There it is one of the inputs of the step [GeoOne holds](/step/geo-one-holds/) of [the Galois row](/proof/galois-row/).
