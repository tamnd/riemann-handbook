---
title: Graded pieces and finite length
decls:
  - CrystallineSemistableComparison.Pb.gr_aff_pf
  - CrystallineSemistableComparison.Pb.wittCohomology_finite_length
  - CrystallineSemistableComparison.Pb.smooth_model_finite_length_link
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Graded pieces and finite length

This section proves two finiteness facts that the comparison uses on both sides of a model. On the generic fibre, which is a smooth scheme over a field of characteristic $0$, the graded pieces of the divided power filtration have no cohomology on an affine open, except in the expected degree. On the special fibre, the crystalline cohomology over the residue field has finite length. The first fact is the local input for the comparison of thickening cohomology with de Rham cohomology and for the finiteness of Hodge cohomology. The second is used, together with the level sequences of the next section ([Theorem 2.11.6](/entry/ls-seq/)), in the Frobenius factorisation of the last section ([Theorem 2.12.6](/entry/fac-ex/)). Both proofs follow the same pattern as the classical ones: reduce to graded pieces, and use a finite cover by charts whose finite intersections are affine.

We keep the notation of the earlier sections. For a scheme $X$ smooth over a ring, a *chart cover* is a finite family of opens $U_\alpha$ that covers $X$, with étale coordinates of dimension $d_\alpha$ on each $U_\alpha$, such that all finite intersections are affine. This is the coordinate cover of section 1 ([Theorem 2.1.9](/entry/hodge-iso-natural-cech/)). For a thickening site with divided power ideal $J$ we write $\mathrm{Fil}^r = J^{[r]}$ and $\mathrm{gr}^r = \mathrm{Fil}^r/\mathrm{Fil}^{r+1}$, as in section 1.

**Definition 2.10.1 (Truncated thickening site).** Let $K$ be a field of characteristic $0$, $X$ smooth over $K$, $s \geq 1$, and $\mathcal{V}$ a set of opens of $X$. The site $\mathrm{KS}(s, \mathcal{V})$ has as objects the divided power thickenings over $K$ (with the trivial divided powers on $K$) whose $s$-th divided power ideal is zero and whose underlying point lands in some $V \in \mathcal{V}$.

The bound $s$ makes the site small enough to compute. Since $J^{[s]} = 0$, the filtration has only $s$ steps, and for $r < s$ the graded piece $\mathrm{gr}^r$ is the same as on the full site.

**Theorem 2.10.2 (Graded pieces on an affine open).** Let $K$ be a field of characteristic $0$, $X$ a smooth scheme over $K$, $V \subseteq X$ an affine open, and $r < s$. Then for every $j \neq r$,
$$H^j\big(\mathrm{KS}(s, \{V\}),\ \mathrm{gr}^r\big) = 0.$$

Lean: `CrystallineSemistableComparison.Pb.gr_aff_pf`.

*Proof.* We take as given a general vanishing principle for truncated thickening sites: if the five facts below hold, then the conclusion of the theorem holds. So it suffices to have the five facts, which we also take as given.

1. *Local graded pieces.* On a frame with constant graded pieces, $H^j(\mathrm{gr}^r) = 0$ for $r < j$, and the classes in degree $r$ are described by differential forms.
2. *Local vanishing.* The cohomology of the quotients $\mathrm{Fil}^r/\mathrm{Fil}^{r'}$ vanishes in the corresponding degrees.
3. *Polynomial thickenings.* A condition on the divided power thickenings of polynomial algebras.
4. *Serre classes.* If the cohomology of each term of a Čech complex lies in a Serre class, then so does the cohomology of the whole.
5. *Covers.* Vanishing passes from all finite intersections of a cover to the cover.

From these five facts, the general statement passes from a chart to an arbitrary affine open $V$: cover $V$ by charts, compute on each finite intersection with hypotheses 1 to 3, and pass to $V$ with hypotheses 4 and 5. $\square$

In classical terms, $H^j(\mathrm{gr}^r) \cong H^{j-r}(V, \Omega^r)$, as in section 1, and this vanishes for $j \neq r$ because $V$ is affine and $\Omega^r$ is quasi-coherent (R. Hartshorne, *Algebraic Geometry*, Theorem III.3.5). The proof above does not use this isomorphism.

The theorem is used four times in the chapter. It shows that the restriction from de Rham cohomology to $\mathrm{KS}(s, \mathcal{V})$ is bijective when $s$ exceeds all chart dimensions, with $\mathrm{Fil}^r$ as the kernel of the map to the quotient. It gives that $\mathrm{Hdg}(a, n)$ is finite-dimensional for proper smooth $X$ and vanishes for $n < a$, which is property 1 of the [period map](/entry/pmap/). It enters the proof that the [top power of the first Chern class](/entry/pow-k-ne-zero/) is not zero. And it enters a finiteness statement for Čech cohomology of graded pieces.

Now we turn to the special fibre. Let $k$ be a perfect field of characteristic $\ell$ and $W(k)$ its ring of Witt vectors, with $W_m(k) = W(k)/\ell^m$. For a ring $O$, a scheme $X$ over $O$ and a ring map $\rho : O \to k$, we write $H^j_m(X)$ for the crystalline cohomology of $X$ along $\rho$ over $W_m(k)$: the cohomology of the structure functor on the site of divided power thickenings over $W_m(k)$. For $m = 1$ the base is $W_1(k) = k$. We measure size by the length of a module (see [[length of a module|CZSCNZH8VY]] and the Background on [modules](/learn/algebra/#rings-ideals-and-modules)).

**Theorem 2.10.3 (Finite length at level one).** Let $k$ be a perfect field of characteristic $\ell$, $O$ a ring, $X$ a proper smooth scheme over $O$, and $\rho : O \to k$ a ring map. Then for every $j$ the $W(k)$-module $H^j_1(X)$ has finite length.

Lean: `CrystallineSemistableComparison.Pb.wittCohomology_finite_length`.

*Proof.* Choose a chart cover $(U_\alpha)$ of $X$, and let $d$ be the maximum of the dimensions $d_\alpha$.

We take as given, from the theory of crystalline cohomology of smooth schemes, the facts in steps 1, 2 and 5 and the filtration principle in step 3.

1. *Vanishing above the dimension.* On the site of thickenings that land in the charts, the cohomology of $\mathrm{Fil}^{d+1}$ vanishes in every degree. So the quotient map $\mathcal{O} \to \mathcal{O}/\mathrm{Fil}^{d+1}$ is bijective on cohomology.
2. *Graded pieces.* For each $r$ and $j$ the cohomology of $\mathrm{gr}^r$ on this site is a finite $W(k)$-module. This step uses that $X$ is proper.
3. *Filtration.* The ring $W_1(k)$ is noetherian. A module with a finite filtration whose graded pieces have finite cohomology has finite cohomology. Apply this to $\mathcal{O}/\mathrm{Fil}^{d+1}$ with the $d + 1$ steps $\mathrm{Fil}^r/\mathrm{Fil}^{d+1}$, and use step 1: $H^j(\mathcal{O})$ on the chart site is a finite module.
4. *Restriction to the cover.* The restriction from the whole site to the site of thickenings that land in some $U_\alpha$ is bijective on cohomology, since the $U_\alpha$ cover $X$. So $H^j_1(X)$ is finite.
5. *Length.* A finite module over $W(k)$ that is killed by $\ell$ is a finite-dimensional $k$-vector space, so it has finite length.

So $H^j_1(X)$ has finite length. $\square$

The comparison uses this in the setting of models. A *residue datum* for $K$ is a perfect field $k$ of characteristic $\ell$, a surjection $\rho : \mathcal{O}_K \to k$, and a ring map $s : k \to \mathcal{O}_{\mathbb{C}_\ell}^\flat$ such that $|s(\rho(x))^\sharp - x| < 1$ for all $x \in \mathcal{O}_K$. Through $s$ and $A_{\mathrm{inf}} \to A_{\mathrm{cris}}$, it gives a map $W(k) \to A_{\mathrm{cris}}$.

**Corollary 2.10.4 (Finite length for smooth models).** Let $(k, \rho, s)$ be a residue datum, $\mathfrak{X}$ a smooth model and $j \geq 0$. Then $H^j_1(\mathfrak{X})$, the crystalline cohomology of $\mathfrak{X}$ along $\rho$ over $W_1(k) = k$, has finite length over $W(k)$.

Lean: `CrystallineSemistableComparison.Pb.smooth_model_finite_length_link`.

*Proof.* A smooth model is proper over $\mathcal{O}_K$, since it is projective, and it is smooth. Apply the theorem on finite length with $O = \mathcal{O}_K$. $\square$

**Remark 2.10.5 (Formalization).** The first theorem is `gr_aff_pf` in [gr_aff.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/GlobalSerreRelations/gr_aff.lean#L14). The file name is in lower case and does not match the theorem, and `gr_aff` in GrCechFin.lean is a second name for it. Its statement is the definition `GrAff` in [GlobSerreSt.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/GlobalSerreRelations/GlobSerreSt.lean#L82). The proof is one application of `GlobalTheory.T.affine_graded_cohomology_vanishing`, whose proof is in `Development/AutomorphicSpectrum/Proofs/BlockDecomposition`; that folder name has no relation to this content. We read the five hypotheses only as statements, and did not unfold their proofs (`locGr_h` and the others in GlobSerreStH.lean). The description of how the general statement passes from charts to $V$ is a reading of the hypotheses, not of the proof. The second and third results are in [SmoothModelFiniteLengthLink.lean](lean:Development/WeilBound/CoreStatements/PadicHodgeComparison/EtaleCohomologyComparison/PerfectoidPullbacks/LocalSystemQuotients/SmoothModelFiniteLengthLink.lean#L42). Steps 1, 2 and 5 of the proof of the theorem on finite length, and the filtration lemma of step 3, are again `GlobalTheory.T` statements with proofs in the same folder, which we did not open. Step 3 is the private lemma `isHecke_div_and_resEtaPow_div` at line 23 of the same file; its name has no relation to Hecke operators or to powers of $\eta$.
