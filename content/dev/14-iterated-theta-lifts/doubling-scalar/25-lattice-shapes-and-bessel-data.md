---
title: Lattice shapes and Bessel data
decls:
  - GlobalTheory.SeeSaw.ShapeExProof.shapeEx
  - GlobalTheory.T.seeSawLatticeShapeExists_proof
  - GlobalTheory.Core.Mi.exists_sBes_scaled_dual
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Lattice shapes and Bessel data

This section constructs two kinds of data that the see-saw arguments of this chapter take as input. The first is a *lattice shape*: self dual lattices for all spaces of a tower, in good position at every place, together with finite combinations of Heisenberg translates at the twist places. It is used in [the shape integral in normal frames](/entry/exists-shape-integral-in-normal-frames-alt/). The second is a *Bessel datum* for the bottom space, with a hyperbolic basis scaled by a free parameter. It is used in [the family of all levels](/entry/fam-all-q-of-all-true-alt/). Both are in the open orbit chapter.

**Setting.** Let $c$ be a valid tower datum with standard character $\psi$. It has spaces $V_j$ and $X_j$ for the steps, a top space $T$, a line space $L_Z$, and for each step $j$, Bessel index $\rho$ and condition $h$, a Bessel space with anisotropic part $V_0(j, \rho, h)$. A *vertex datum* $v$ gives lattices $N_j$ of $V_j$ and $N_T$ of $T$, a finite set $P_g$ of good places, a finite set $P_t$ of twist places, maps $\tau_j$, finite combinations $d_j$ and ramified sets. Let $k$ be a nonarchimedean local field. *Twist data* $o$ over $k$ give split places $p_i$ of $E$ with completion $k$ for $i$ in a list $I$, frames $\beta_j(i)$ and lattice pairs $Q_j(i)$ at these places, lattices $M(j, \rho, h)$ of the anisotropic parts, glued frames $\beta_0$, a uniformizer and ramified sets. We use four local conditions at a place $x$:

1. *pre-twist*: the list $I$ has no repeats and contains every index, the places $p_i$ are distinct and are exactly $P_t$, the characters are standard at $p_i$, and the frames, line vectors and norms at the top have the required shape;
2. *good at $x$*: the lattices $N_j$, $M(j, \rho, h)$ and $N_{j+1}$ are in good position for the Bessel and Fourier-Jacobi steps at $x$;
3. *split at $x$*: each $M(j, \rho, h)$ is an orthogonal sum at $x$ of the lattice of the step and a self dual lattice of the line part, and the same holds at the top step;
4. *glued core*: at each twist place, $M(j, \rho, h)$ and $\beta_0$ give a glued frame of the Bessel step.

A lattice shape for $(v, o)$ is *off the twist places* if $v$ and $o$ are pre-twist, good at every place, split at every place outside $P_t$, glued at every twist place, and if, for $j < m$ and every vacuum $f$ for the integral lattices of the steps, the combination of $d_j$ applied to $f$ is the product over $i \in I$ of the indicator functions of the pairs $(Q_j(i), Q_{j+1}(i))$ applied to $f$. It also requires the ramified sets of $v$ and $o$ to agree.

**Theorem 2.25.1 (Lattice shapes exist).** Let $c$ be valid, let $v$ be a vertex datum and $o$ twist data. Assume that $P_g$ and $P_t$ are disjoint, $N_T$ is self dual, $v$ and $o$ are pre-twist, $N_j$ is self dual for $j < m$, $(v, o)$ is good and split at every place of $P_g$, and that at the top step there is, for every place $x \notin P_t$, a self dual lattice of $L_Z$ that splits the top lattice at $x$. Then there are lattices $N'_j$, finite combinations $d'_j$ at the twist places, lattices $M'$ and glued frames $\beta'_0$ such that:

1. $N'_j$ is self dual for $j < m$, and equals $N_j$ at every place of $P_g$;
2. $M'(j, \rho, h)$ equals $M(j, \rho, h)$ at every place of $P_g$;
3. the new data are a lattice shape off the twist places, with the ramified sets of $v$ replaced by those of $o$.

Lean: `GlobalTheory.SeeSaw.ShapeExProof.shapeEx` (also `GlobalTheory.T.seeSawLatticeShapeExists_proof`, a second name).

*Proof.* We first find lattices in good position everywhere, then patch them at $P_g$.

1. *Good position at all places.* By the theorem on lattices in good position at all places, there are self dual $N^0_j$, lattices $M^0$ and glued frames $\beta_0$ that are good at every place, split at every place outside $P_t$, and glued at every twist place.
2. *No good places.* If $P_g$ is empty, take $N^0$ and $M^0$.
3. *Patching.* Otherwise, pick $x_0 \in P_g$. The lattices $M$ and $M^0$ are self dual, by the good position at $x_0$. By the theorem on self dual lattices patched at places, there are self dual $N'_j$ equal to $N_j$ at $P_g$ and to $N^0_j$ elsewhere, and self dual $M'$ equal to $M$ at $P_g$ and to $M^0$ elsewhere.
4. *Locality.* By the theorem that good position and split lines are read on completions, these conditions at $x$ depend only on the completions at $x$ of the lattices. At $x \in P_g$ they hold by hypothesis, and at $x \notin P_g$ they hold by step 1.
5. *Glued cores.* The twist places are not in $P_g$, since the two sets are disjoint. So $M'$ equals $M^0$ at the twist places, and the glued cores of step 1 carry over.
6. *Combinations.* For $j < m$, the theorem on data as combinations at split places gives a finite combination $d'_j$ at the twist places with the required action on vacua. It uses the standard character and the self duality of the step lattices. For $j \geq m$, take $d'_j = 0$.
7. *Ramified sets.* The new vertex datum takes its ramified sets from $o$, so they agree. $\square$

**Theorem 2.25.2 (Bessel data with a scaled dual basis).** Let $X$ be a Hida setting whose instance is that of the tower datum $D$, with the embedding of $E$ the identity. Let $u$ be a word, $\psi$ a standard character of sign $-1$, and $F_0$ step zero forms with a transport $\mathrm{tr}$. Then there is $\lambda \in E$ with $\lambda = g$ or $\lambda = -g$, where $g$ is the level of $X$, such that the following holds. For every nonzero $\mu \in E$ and every volume datum $v_A$ of $X_0$, there is a Bessel datum $B$ of $(X, u, \psi)$ with anisotropic space $X_0$ such that:

1. $B$ is adapted to the weight of $\mathrm{tr}$: the embedding of $X_0$ into $Y_0$ has the coordinates of the transported frame of $\mathrm{tr}$ as its columns; and the volume datum of $B$ is $v_A$;
2. the line vector of $B$, embedded in $Y_0$, is $\mu z_u$, where $z_u$ is the row vector of $u$;
3. for $1 \leq a \leq r_S$, the hyperbolic vectors of $B$ are
$$e_a = \mu\, \lambda^{\,r_S - a}\, e^R_a, \qquad e'_a = \overline{\big(\mu\, \lambda^{\,r_S - a}\big)}^{\,-1}\, f^R_a,$$
where $e^R_a$ and $f^R_a$ are the reference vectors of $X$.

Lean: `GlobalTheory.Core.Mi.exists_sBes_scaled_dual`.

The dual vectors are scaled by the inverse conjugate, so the pairing of $e_a$ with $e'_a$ is that of $e^R_a$ with $f^R_a$.

*Proof.* We build $B$ from a line, a decomposition and a rescaled hyperbolic decomposition.

1. *Sign.* By the theorem on the sign of the $\psi$ tie, there is $\lambda = \pm g$ such that the character condition of a Bessel datum holds for every $\mu \neq 0$ and every decomposition with the hyperbolic vectors of item 3. Since $g \neq 0$, $\lambda \neq 0$.
2. *Line.* There is a line $L$ of rank $1$ with a vector $\zeta$ and a nonzero $t \in E$ that ties $\zeta$ to $z_u$.
3. *Orthogonal sum.* There is an orthogonal decomposition $V_0 = X_0 \oplus L$.
4. *Hyperbolic decomposition.* There is a decomposition $d_0$ of $Y_0$ with anisotropic part $V_0$ that maps $\zeta$ to $t z_u$ and has the hyperbolic vectors of item 3 for $\mu = t$.
5. *Rescaling.* Multiply the vectors $e$ of $d_0$ by $\mu t^{-1}$ and the vectors $e'$ by the inverse conjugate. This keeps all the relations of a decomposition. Scale $\zeta$ by $\mu t^{-1}$; it is still a line vector. The new data have the vectors of items 2 and 3.
6. *Ties.* The unipotent radical of the flag is the subgroup of the second model, and the image of the anisotropic embedding is the second model subgroup, by two cited theorems. The character tie is step 1. The space $X_0$ is cocompact, and a volume datum of the unipotent part exists.
7. *Adaptation.* The embedding of $V_0$ into $Y_0$ in $d_0$ is given by the transported frame, and the embedding of $X_0$ into $V_0$ is a section of the projection onto $X_0$ that the projection onto $L$ kills. So the composite has the columns of item 1. Rescaling does not change it. $\square$

**Remark 2.25.3 (Formalization).** The shape theorem is at [SeeSawLatticeShapeExistsProof.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLatticeShapeExistsProof.lean#L30), and its second name is in [SeeSawLatticeShapeExistsProofStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawLatticeShapeExistsProofStatement.lean#L6), by a `first | exact` block under one million heartbeats. The shape conditions are in [VacOfShape.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/VacOfShape.lean#L88), and the claim at line 122 of that file. The claim replaces the ramified sets of $v$ by those of $o$ (line 132), so the condition that they agree holds by definition (line 96 of the proof). The hypotheses that $N_T$ is self dual and that the top lattices split are used only in step 1. The Bessel theorem is at [ExistsSBesUnscaledDual.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ExistsSBesUnscaledDual.lean#L50), with the rescaling of step 5 at line 30. The file name says "unscaled", but the theorem is the scaled form; the unscaled forms with $\mu = 1$ are corollaries at lines 61 and 68 of the same file. Bessel data are in [ThetaIdentityOfMapsAll.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/ThetaIdentityOfMapsAll.lean#L105). We have read the statements, not the proofs, of the cited theorems on good positions, patching, completions, combinations, the sign of the tie and the second model.
