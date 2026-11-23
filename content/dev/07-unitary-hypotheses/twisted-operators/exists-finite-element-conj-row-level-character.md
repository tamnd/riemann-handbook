---
id: exists-finite-element-conj-row-level-character
title: A finite element conjugates the row level onto the Hida level
kind: theorem
decl: GlobalTheory.T.exists_finite_element_conj_rowLevel_character
module: Development.AbelianVarietyTheory.Proofs.TwistedOperators.ExistsFiniteElementConjRowLevelCharacterStatement
covers: 306
status: drafted
drafted_by: writer@claude
---
This theorem is a second name. It is the first step of [the row placement](/entry/row-placement-exists/): it gives the finite element $t$ that the later steps use. Its proof calls one lemma with the same statement. The real content is in [the conjugation of levels](/entry/exists-conj-level/).

## Statement

Let $V = Y_0$ be the first row space, $G_f^c$ the adelic unitary elements with trivial archimedean part, and $K = \mathrm{levS}(V, \beta_Y, L)$ with character $\chi = \mathrm{levChi}(V, \beta_Y, L)$, where $L$ is the level data of the true row. Assume that $R$ satisfies the level hypotheses, the group hypotheses and the model hypotheses. Then there is $t \in G_f^c$ such that:

- for every $k$, $k \in K$ if and only if $t k t^{-1} \in \iota^{-1}(1, K_2)$, and then $\chi(k) = \overline{\chi_2(t k t^{-1})}$;
- the moved frame $t \beta_Y$ is a frame for the base lattice $L_0$ of $V$.

Here $\iota$ is `iotaX X h`, and $K_2$, $\chi_2$ are the level group and character of the Hida setting $X$.

## Proof

The proof is `first | exact @GlobalTheory.SeeConj.exists_conj_level | ...`. It applies the lemma `SeeConj.exists_conj_level`, which has the same statement.

## In the Lean code

The theorem is in [ExistsFiniteElementConjRowLevelCharacterStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsFiniteElementConjRowLevelCharacterStatement.lean#L12). The lemma is in [ExistsFiniteElementConjRowLevelCharacter.lean](lean:Development/AbelianVarietyTheory/Proofs/TwistedOperators/ExistsFiniteElementConjRowLevelCharacter.lean#L17). The hypothesis `R.IsModels` is not used by that lemma.
