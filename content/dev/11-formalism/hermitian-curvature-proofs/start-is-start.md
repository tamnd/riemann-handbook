---
id: start-is-start
title: The start matrix is a start
kind: theorem
decl: Formalism.FourierDecayAlt.P.MAx1.startIsStart
module: Formalism.HermitianCurvature.HermitianCurvatureProofs.CoordinateCommuteRaisingConstant
covers: 455
status: drafted
drafted_by: writer@claude
---
This theorem says that the $2 \times 2$ matrix of model operators in [the start data at a model level](/entry/start-ok/) satisfies four conditions `IsStart`: it is Hermitian, it satisfies an RTT relation, it satisfies a determinant relation with the scalar $q$, and $q$ is real. It is the first of the ten fields there. The proof is an assembly of three proved facts and a sign lemma. The real content is in those three facts.

## Statement

Use the parameters $P$, the algebra $D$, the sign $s = (-1)^{k-l}$, the matrix $Q_r(Y) = \begin{pmatrix} t_{11}(Y) & t_{12}(Y) \\ t_{21}(Y) & t_{22}(Y)\end{pmatrix}$ and the scalar $q$ of [the start data at a model level](/entry/start-ok/). Let $Q = s\,Q_r$. Let $\mathcal{P}$ be the flip on $\mathbb{C}^2 \otimes \mathbb{C}^2$, let $Q_1 = Q \otimes 1$ and $Q_2 = 1 \otimes Q$, and let $J = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}$.

**Theorem.** If `P.OK` and `D.Laws P.TT` hold, then for each $l$:

1. $Q(Y)^* = Q(Y)$ for real $Y$, with $^*$ the conjugate transpose;
2. $(Y' - Y - \mathcal{P})\,Q_1(Y')\,Q_2(Y) = Q_2(Y)\,Q_1(Y')\,(Y' - Y - \mathcal{P})$ for all $Y$, $Y'$;
3. $Q(Y+1)^{T} J\,Q(Y) = q(Y)\,J$ and $Q(Y)\,J\,Q(Y+1)^{T} = q(Y)\,J$ for all $Y$;
4. $\overline{q(Y)} = q(Y)$ for real $Y$.

Item 2 is the defining relation of the Yangian $Y(\mathfrak{gl}_2)$, with the $R$-matrix $u - \mathcal{P}$ (Molev, *Yangians and Classical Lie Algebras*, 2007, chapter 1).

## Proof

The proof first proves the four items for $Q_r$:

1. `qQHerm` says $Q_r(Y)^* = Q_r(\bar Y)$. At real $Y$ this is item 1.
2. `qQRTT` gives item 2. It comes from the entry form $(u - v)[Q_{ij}(u), Q_{kl}(v)] = Q_{kj}(u)Q_{il}(v) - Q_{kj}(v)Q_{il}(u)$, which is proved from five relations between the shifts, $\nabla$ and the curvature.
3. `qQDet` gives item 3. It uses twelve proved facts.
4. `qC_real` gives item 4.

Then `isStart_smul` moves the result to $s\,Q_r$. Since $\bar s = s$, item 1 holds. In item 2 both sides get the factor $s^2$. In item 3, $s^2 = 1$. We have not unfolded the proofs of `qQHerm` and `qQDet`.

## In the Lean code

The theorem is at [CoordinateCommuteRaisingConstant.lean](lean:Formalism/HermitianCurvature/HermitianCurvatureProofs/CoordinateCommuteRaisingConstant.lean#L6100). It is `startIsStartAssemble qQHerm qQRTT qQDet`, with the assembly at line 5769 and `isStart_smul` at line 5186. `qQHerm` at line 1711 only renames the theorem of the same name at line 1228, in the namespace `D5`. `IsStart` is in [StatementWd.lean](lean:Formalism/HermitianCurvature/StatementWd.lean#L79), and `IsRTT` and `IsDet` in [StatementW.lean](lean:Formalism/HermitianCurvature/StatementW.lean#L9).
