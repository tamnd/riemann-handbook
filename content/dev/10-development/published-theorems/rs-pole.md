---
id: rs-pole
title: The pole of the Rankin-Selberg L-function, from closed inputs
kind: theorem
decl: PositivityTheory.AdelicQuotientData.rsPole
module: Development.WeilBound.CoreStatements.PublishedTheorems.JacquetShalikaRigidity.JacquetShalikaRigidity
covers: 985
status: drafted
drafted_by: writer@claude
---
This theorem proves `RSPole`, a statement about the partial Rankin-Selberg L-function of two cuspidal representations near $s = 1$. It sits below the step [EveryCharacter](/step/every-character/). The proof only applies [`rsPole_of_inputs`](/entry/rs-pole-of-inputs/) to 22 theorems of the code. The content is in that entry. Below this theorem are 985 declarations.

## Statement

Let $E$ be a totally complex number field. Let $\pi$ be a cuspidal subrepresentation of $\mathrm{GL}_m$ over $E$ and $\pi'$ one of $\mathrm{GL}_k$, with $1 \le k \le m$, and let $u \in \mathbb{R}$. Suppose that $\pi$ and $\pi'$ are normalised (`IsNormalised`, invariance under the split centre). For a finite set $S$ of places, let $\alpha_w$ and $\beta_w$ be the Satake parameters of $\pi$ and $\pi'$ at the places $w \notin S$, and let
$$L^S(s) = \prod_{w \notin S} \prod_{a,b} \bigl(1 - \alpha_{w,a}\, \overline{\beta_{w,b}}\, q_w^{-s}\bigr)^{-1}.$$
In the code this is `LS S α β s`.

**Theorem.** There is a finite set $S_0$ such that for every $S \supseteq S_0$ and all such $\alpha$, $\beta$ there are functions $Z$ and $Z_S$ and a real $\sigma_0$ with:

1. $Z$ and $Z_S$ are holomorphic on $\operatorname{Re} s > 0$;
2. $Z_S(\sigma + iu) \neq 0$ for all $\sigma > 0$;
3. $Z(s) = (s - 1)\, Z_S(s)\, L^S(s)$ for $\operatorname{Re} s > \sigma_0$;
4. if $(m, \pi) \neq (k, \pi')$, then $Z(1) = 0$.

For unitary $\pi'$, $L^S(s)$ is $L^S(s, \pi \times \pi'^\vee)$. If $\pi \neq \pi'$, the factor $s - 1$ cancels. This matches the result of Jacquet and Shalika that $L^S(s, \pi \times \pi'^\vee)$ has no pole at $s = 1$ when $\pi \not\cong \pi'$ (Amer. J. Math. 103, 1981).

## Proof

The proof is `rsPole_of_inputs` with 22 arguments. Most are theorems of the namespace `jumpWindows`, such as `multiplicity_one_holds`. The others are `cauchyAll` (the Euler product for $L^S$ converges for $\operatorname{Re} s > 2$), `JacquetShalikaLocal.l7`, `l12` and `jacquetShalikaBound` (the bound $|\alpha_{w,a}| \le q_w^{1/2}$).

## In the Lean code

The theorem is in [JacquetShalikaRigidity.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/JacquetShalikaRigidity/JacquetShalikaRigidity.lean#L10). `RSPole` is in [CauchyLoc.lean](lean:Development/WeilBound/RepresentationTheoryGL/JacquetShalikaBounds/AbsoluteRigidity/CauchyLoc.lean#L46).

The code uses it three times. `jacquetShalikaRigidity` in the same file is `rigid rsPole jacquetShalikaBound`. [ListOfMultiset.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/ListOfMultiset.lean#L51) and [SysEx.lean](lean:Development/AutomorphicArithmetic/Foundations/Convolution/NormCharacterPowers/SysEx.lean#L13) use it as `rankin_selberg_unitary_of_pole norm_exponent_equality satake_twist_holds rsPole`, which proves `RSU`. In `RSU`, $u$ becomes the difference of the twists of $\pi$ and $\pi'$.

The statement does not claim a pole when $\pi = \pi'$. It only bounds the order of the pole by one. Also, $Z_S$ is only known to be nonzero on the line $\operatorname{Im} s = u$.
