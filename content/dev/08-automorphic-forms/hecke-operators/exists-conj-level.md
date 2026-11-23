---
id: exists-conj-level
title: Moving the row frame onto the Hida level
kind: theorem
decl: GlobalTheory.SeeConj.exists_conj_level
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsFiniteElementConjRowLevelCharacter
covers: 305
status: drafted
drafted_by: writer@claude
---
This lemma proves [the conjugation of the row level](/entry/exists-finite-element-conj-row-level-character/), which is a second name for it. It finds a finite unitary element $t$ that moves the self-dual frame of the first row space to a frame of the base lattice, and that carries the row level group with its character onto the Hida level group. The result goes up to [the row placement](/entry/row-placement-exists/).

## Statement

The statement is the one in the parent entry. In short: there is $t \in G_f^c$ such that $k \mapsto t k t^{-1}$ carries $K = \mathrm{levS}(V, \beta_Y, L)$ onto $\iota^{-1}(1, K_2)$, the character $\mathrm{levChi}$ goes to $\overline{\chi_2}$, and $t \beta_Y$ is a frame of the base lattice $L_0$.

## Proof

The proof is a change of frame in four moves.

1. The group hypothesis `hGrp.levels` gives a generic $\psi_0$ and a permutation $\pi$ that reorders the level data of the true row into the symmetric level data $P^\sharp(\psi_0)$.
2. `exists_frame_conjugate_level_symmetricLevel` gives a frame $\beta_3$ of the base lattice. Its level group for $P^\sharp(\psi_0)$ is $\iota^{-1}(1, K_2)$, with character $\overline{\chi_2}$. `exists_frame_reordering_levelData` uses $\pi$ to give a frame $\beta_2$ whose level group and character for the true row data agree with those of $\beta_3$.
3. The level hypothesis says that $\beta_Y$ is a self-dual frame. `exists_finiteUnitary_selfDualFrame_to_baseLatticeFrame` gives $t_0 \in G_f^c$ such that $t_0 \beta_Y$ is a frame of the base lattice. The level places are pairwise not conjugate (`levelPlaces_not_isConjPlace_realDat`). So `exists_unitary_matching_frames_at_nonconjugate_places` gives $u \in G_f^c$ such that $u t_0 \beta_Y$ is still a frame of the base lattice and has the same reductions as $\beta_2$ at every level place.
4. Put $t = u t_0$. Conjugation by $t$ carries the level of $\beta_Y$ to the level of $t \beta_Y$ (`levelSubgroup_conj_finite_moves_frame`). Two frames with the same reductions at the level places give the same level group and character (`levS_iff_and_levChi_eq_of_redFn_eq`, with an empty set of extra places). Chain this with step 2.

## In the Lean code

The lemma is in [ExistsFiniteElementConjRowLevelCharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsFiniteElementConjRowLevelCharacter.lean#L17). Each named lemma is called through a statement file that applies a lemma of another namespace, for example `SeeConj.exists_frame_symLevel` and `FrameMatch.frames_match`. We have not opened those proofs. `IsFrame` is in [DefGroup.lean](lean:Formalism/LocalToGlobal/Divisibility/DefGroup.lean#L467).

The hypothesis `R.IsModels` is introduced as `_hMod` on line 18 and is never used. The parent statement still asks for it.
