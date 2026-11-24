---
title: The model statement
decls:
  - GlobalTheory.ExpModel.modelSt_of_small_frame_gal
  - GlobalTheory.T.model_statement_of_crystalline_chebotarev_frame_gal
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The model statement

This section turns the frames of Section 5 and the Galois representations of Section 7 into $\ell$-adic Hida settings that cover the block subspace at a small twisted place. The settings are indexed by the maximal ideals of the Hecke algebra of the frame that meet the block, and each of them carries the inputs that the exponent bound needs: the prime $\ell$ is not a unit in its coefficient ring, and its Galois data are linked to the weights. Two published theorems enter here: the Chebotarev density theorem in degree one, and the theorem of Bhatt and Scholze on crystalline lattices. The result feeds [the exponent bound](/entry/exponent-bound-of-unitary-theta-standard-theorems-alt/) of Section 9. The background is in [crystalline representations](/learn/galois-representations/#crystalline-de-rham-and-potentially-semistable-representations).

We first state the two inputs.

**Theorem 5.8.1 (Chebotarev in degree one).** Let $F$ be a number field with an algebraic closure $\Omega$, and $L \subseteq \Omega$ a finite Galois extension of $F$. Let $g \in \mathrm{Gal}(L / F)$ and let $S$ be a finite set of finite places of $F$. Then there is a finite place $v \notin S$ of residue degree $1$ over $\mathbb{Q}$, with a place of $\Omega$ above it whose inertia group fixes $L$, and a Frobenius element $\sigma$ at that place whose restriction to $L$ is $g$.

Lean: `GlobalTheory.Published.ChebotarevDegreeOne`.

This follows from the Chebotarev density theorem (Neukirch, *Algebraic Number Theory*, Chapter VII, §13), since the places of degree $1$ have density $1$ among all places.

**Theorem 5.8.2 (Crystalline lattices).** Let $\ell$ be a prime and $K$ a finite extension of $\mathbb{Q}_\ell$, with a fixed prism of $\mathcal{O}_K$ identified with $A_{\inf}$. Then:

1. for each finite extension $L$ of $\mathbb{Q}_\ell$ and each $G_K$-stable $\mathcal{O}_L$-lattice $T$ in a crystalline representation of $G_K$, there is an $F$-crystal $\mathcal{E}$ over $\mathcal{O}_K$ that realizes $T$;
2. for two lattices $T$ and $T'$ realized by $F$-crystals $\mathcal{E}$ and $\mathcal{E}'$, each $G_K$-equivariant $\mathbb{Z}_\ell$-linear map $f \colon T \to T'$ comes from a unique map of $F$-crystals $\mathcal{E} \to \mathcal{E}'$.

Lean: `GlobalTheory.Published.BhattScholzeCrystallineLattices`.

This has the shape of the theorem of Bhatt and Scholze (*Prismatic $F$-crystals and crystalline Galois representations*, 2023), which identifies crystalline $\mathbb{Z}_\ell$-lattices with prismatic $F$-crystals.

Now the conclusion. Keep the notation of Section 5. A *Hida setting* of rank $N$ for the weights $\lambda$ is an $\ell$-adic setting with a coefficient ring $\mathcal{O}$ and an inclusion property at each level $J \ge 0$. For the block at $(j, t)$ there are two lattices in the block subspace $Z$: the *cut lattice* and the *second lattice*. At a level $J$ the *inclusion at $w$* holds if

$$\ell^{J} \cdot \operatorname{cut}(Z) \subseteq \operatorname{second}(Z)_w,$$

where the right side is the localization at $w$. A family $(X_i)_{i \in I}$ of Hida settings *covers* $Z$ at $w$ if, for each $J$, the inclusion of all $X_i$ at level $J$ implies the inclusion at $w$ at level $J$.

**Definition 5.8.3 (Model statement).** The *model condition* at $w$ holds if there are maps $\mathrm{fr}$ and $\mathrm{cj}$ on the infinite types, an index set $I$ and Hida settings $X_i$ of rank $N_r$ for the weights $\lambda$ of $W$, such that the $X_i$ cover $Z$ at $w$ and, for each $i$, $\ell$ is not a unit in the coefficient ring of $X_i$ and the inputs of $X_i$ are linked to $P$ and to $W$ with $\mathrm{fr}$ and $\mathrm{cj}$ at $\ell$. The *model statement* is the model condition at each twisted place, in range.

Lean: `GlobalTheory.ExpTie.ModelStatement` (also `GlobalTheory.ExpTie.ModelAt`, the condition at $w$).

**Theorem 5.8.4 (The model statement).** Assume Chebotarev in degree one and the theorem on crystalline lattices. Then the smallness condition, the frame statement and the Galois statement imply the model statement.

Lean: `GlobalTheory.ExpModel.modelSt_of_small_frame_gal` (also `GlobalTheory.T.model_statement_of_crystalline_chebotarev_frame_gal`, a second name).

*Proof.* Statements in range are closed under conjunction, so in range the three statements hold together. Fix a rich point $p$, a level $j$, a pair $(P, W)$ that passes the checks, and a twisted place $w$ with $W$ in range at $\ell$, beyond all thresholds.

By smallness, $\ell$ is prime and $N_r + 1 < \ell$. The numerical checks give $N_r \ge 1$, so $\ell \ne 2$. The frame statement gives a good frame $F$ of rank $N_r$, a reading $R$, embeddings $\mathrm{inc}$ and a tie $T$, and the Galois statement gives the Galois side for them.

1. *Lattice link.* From the theorem on crystalline lattices, $\ell \ne 2$, $\ell \nmid \operatorname{disc} E$ and the half system of $T$, [the lattice link of block data](/entry/crystalline-lattice-link-of-block-data/) gives maps $\mathrm{fr}$ and $\mathrm{cj}$ and a link between crystalline lattices and the weights, for each pair that passes the checks.
2. *Hecke module.* There is a level map for $F$ and the weights $\lambda$, and with it the frame has a Hecke module on the lattice of the weights.
3. *Index set.* Let $I$ be the set of maximal ideals $\mathfrak{m}$ of the Hecke algebra of $F$ such that some eigensystem $\theta$ that occurs in $Z$ through $R$ lies over $\mathfrak{m}$. For $\mathfrak{m} \in I$ let $X_{\mathfrak{m}}$ be the Hida setting of $F$ at $\mathfrak{m}$. Since $Z$ lies in the space of the block operators, the settings over the maximal ideals that meet $Z$ cover $Z$ at $w$.
4. *Inputs.* Fix $\mathfrak{m} \in I$ with $\theta$ over it. The coefficient ring of the frame has finite quotient at $\ell$, and $\ell$ is not a unit in it. The block operators send the subspace $Z$ into itself, so $\theta$ lies in the block. Then [the inputs of a frame](/entry/winputs-frame/) give the link of $X_{\mathfrak{m}}$ from Chebotarev in degree one, the Galois side, the lattice link of step 1, the Hecke module of step 2 and the fact that $\theta$ lies in the block over $\mathfrak{m}$.

So $(\mathrm{fr}, \mathrm{cj}, I, X)$ is a witness of the model condition at $w$. $\square$

Chebotarev is used in step 4 to separate the eigensystems by their Frobenius traces: two eigensystems in the block over the same $\mathfrak{m}$ give the same Galois representation modulo $\mathfrak{m}$, and the places of degree one detect this. The crystalline lattices are used in step 1 to compare an integral structure of the Galois representation of Section 7 with the integral structure of the weights. This is our reading of the role of the two inputs; the lemmas that use them are not opened here.

The smallness condition and the frame statement are proved with no input (Sections 5 and 9), so at the point of use only the two published theorems and the Galois statement are real hypotheses.

**Remark 5.8.5 (Formalization).** The theorem is in [ModelStOfFrames.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStOfFrames.lean#L30), with `maxHeartbeats` set to 1600000, and its second name in [ModelStOfFramesStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStOfFramesStatement.lean#L12), a one-line call with `maxHeartbeats` set to 1000000. The statement is in [ModelStatement.lean](lean:Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ModelStatement.lean#L26), and the condition at a place, the cover and the inclusion in [SumExpSt.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/SumExpSt.lean#L77). There is a second definition named `ModelStatement` in `GlobalTheory.ShareOn`, the run model statement of Section 3; the two are unrelated. The proof is the same, line for line, as that of a theorem in [ModelStatementOfFrameGalois.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ModelStatementOfFrameGalois.lean#L117), which uses the older wrapper for statements at points; only the wrapper differs. The Chebotarev input in Lean asks for residue degree $1$ over $\mathbb{Z}$, and it is shown equivalent to a second form of Chebotarev in ChebotarevDegreeOneIffCheb.lean. We have not unfolded the Hida setting, the link of inputs, the cut and second lattices, or the prisms and $F$-crystals of the Bhatt-Scholze statement; the statement of that input above is our reading of its Lean type, and we have not checked it against the published theorem.
