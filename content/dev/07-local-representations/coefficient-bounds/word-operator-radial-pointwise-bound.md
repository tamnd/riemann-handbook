---
id: word-operator-radial-pointwise-bound
title: The radial pointwise bound for word operators (restatement)
kind: theorem
decl: GlobalTheory.T.wordOperator_radial_pointwise_bound
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.WordOperatorRadialPointwiseBoundStatement
covers: 302
status: drafted
drafted_by: writer@claude
---
This theorem is a restatement. It gives the radial bound for word operators a name in the namespace `GlobalTheory.T`. Its caller [`HatNF.wordBound_cptCoef`](/entry/word-bound-cpt-coef/) uses it once, as step 2 of its proof. The real content is in [`HatNF.RadBound.word_bound`](/entry/word-bound/).

## Statement

**Theorem.** Let $X, \mu, L, \mathrm{st}, l_0$ be data that satisfy `P5.IsData`, and let $d$ be normal form data for $X$ (`IsNF X d`). Let $T$ be a set of radial operators and $a \in \mathbb{N}$ such that each basic element of $d$ lies in $\mathrm{nfSpan}(d, T, 0, a, 1)$. Let $w$ be an admitted word of length $N$. Then there are $C \ge 0$, $J$ and a list of lists $H$ of $N$ elements of $T$ such that, for each multiplier family $W$ of a function $\varphi$ with $\varphi \circ \exp$ smooth, each radial function $\Phi$, each index $e$ and each radial point $x$,

$$\|M_{w,e}(W_0\Phi)(x)\| \le C\, d_R(x)^{-N} g_R(x)^{-aN} \sum_{j=0}^{J} |\vartheta^j\varphi(g_R(x))| \sum_{H} \Bigl\|\Bigl(\prod H\Bigr)\Phi(x)\Bigr\|.$$

The [entry of the proof](/entry/word-bound/) defines $M_{w,e}$, $d_R$, $g_R$ and $\vartheta$.

## Proof

The statement is the same text as the statement of `HatNF.RadBound.word_bound`. The proof is that theorem. There is no other step.

## In the Lean code

The theorem is in [WordOperatorRadialPointwiseBoundStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordOperatorRadialPointwiseBoundStatement.lean#L6). The proof is the tactic `first | exact @… | exact … | (intros; apply … <;> assumption)`, with `HatNF.RadBound.word_bound` in each branch. The file sets `maxHeartbeats` to 1000000.
