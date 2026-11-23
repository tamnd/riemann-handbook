---
id: angehrn-siu-not-klt-at-several-points
title: A combination of sections that is not klt at several points, second name
kind: theorem
decl: GlobalTheory.T.angehrnSiu_not_klt_at_several_points
module: Development.AbelianVarietyTheory.Proofs.DivisorProofs.AngehrnSiuNotKltAtSeveralPointsStatement
covers: 478
status: drafted
drafted_by: writer@claude
---
This theorem is a second name for [`LocalHeart.not_klt_at_points`](/entry/not-klt-at-points/). It has no proof of its own. Its only use is in step 5 of [the inductive step of Angehrn-Siu](/entry/exists-global-step/), which gives it local equations of sections of $\mathcal{O}(lA)$ at the points of $P$ and gets a nonzero vector $a \in \mathbb{C}^l$.

## Statement

The statement is the same text as that of [`not_klt_at_points`](/entry/not-klt-at-points/), where it is given in full. In short: assume principalisation. Let $R_1, \dots, R_c$ be local rings of points of a normal variety with function field $K$, with residue maps $\pi_i$ onto local rings of a field $\kappa$ of transcendence degree $k \geq 1$. Let $w_{ij}$ be elements of $R_i$ whose images are $\lambda_i \bar{w}_j$. If $c \binom{M+k-1}{k} < l$ and $M \geq 1$, then there is a nonzero $a \in \mathbb{C}^l$ such that, at each $i$, the pair $\varphi + t \operatorname{div}(\sum_j a_j w_{ij} + u)$ is not klt when $t$ is large enough in terms of $M$ and $k$.

## Proof

The proof is one line: `exact @LocalHeart.not_klt_at_points`, inside a `first` combinator.

## In the Lean code

The theorem is at [AngehrnSiuNotKltAtSeveralPointsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/AngehrnSiuNotKltAtSeveralPointsStatement.lean#L12). The real content is in [`not_klt_at_points`](/entry/not-klt-at-points/).
