---
id: laws-of-pin-resc
title: The twist place laws for pinned tuples rescaled by roots of unity
kind: theorem
decl: GlobalTheory.QTw.laws_of_pin_resc
module: Development.AbelianVarietyTheory.Proofs.DecoratedLatticeProofs.SeeSawTwistPlaceLawsOfRootOfUnityRescaling
covers: 1073
status: drafted
drafted_by: writer@claude
---
This theorem proves three laws at the twist places for a decorated tuple that is a pinned tuple up to scalars. Its only user is the restatement [`seeSawTwistPlaceLaws_of_rootOfUnityRescaling`](/entry/see-saw-twist-place-laws-of-root-of-unity-rescaling/), which [`laws_resc_alt`](/entry/laws-resc-alt/) calls. This is in branch 3 of the [unitary hypotheses chapter](/proof/unitary-hypotheses/), which gives the multiplicity condition.

## Statement

Fix a datum $D$, a common datum $c$, level data $v$ and a tuple $t$. A decorated tuple $w$ over $t$ (`VTup t`) holds a finite set $Q$ of places, finitely supported coefficient vectors $e_Q(j)$, $d_Q(j, \alpha, \gamma)$, $\varepsilon(j, \alpha)$ and $\varepsilon_T(n, \beta)$, sets $F_X$, $F_Y$, $F_T$ of test functions, and constants $c_Q(j)$. Here $\alpha$, $\gamma$, $\beta$ run over finite index sets $\mathrm{Ch}_j$ of characters.

- $w$ is *pinned* (`QPin v w`) if there are local data $Q_1, \dots, Q_r$ at distinct split places, with union $Q$, such that $e_Q$, $d_Q$, $\varepsilon$, $\varepsilon_T$ and $c_Q$ are convolution products of the local data, with weights. The pin says nothing about $F_X$.
- For scalars $s_j(\alpha) \in \mathbb{C}$, the rescaled tuple $\mathrm{resc}(w, s)$ replaces $d_Q(j, \alpha, \gamma)$ by $s_j(\alpha)\, s_{j+1}(\gamma)^{-1} d_Q(j, \alpha, \gamma)$, $\varepsilon(j, \alpha)$ by $s_j(\alpha)\, \varepsilon(j, \alpha)$, and $\varepsilon_T(n, \beta)$ by $s_n(\beta)\, \varepsilon_T(n, \beta)$.
- `QPinU v w` holds if $w = \mathrm{resc}(w_0, s)$ for a pinned $w_0$ and scalars with $s_j(\alpha)^n = 1$ for some $n > 0$.

The three laws are statements about $v$ and $w$:

- `QLaw`: an identity of iterated integrals. For each middle step $j$, a sum over $\alpha$ of periods weighted by the coefficients of $\varepsilon(j, \alpha)$ equals $c_Q(j)$ times a sum over $\beta$ of periods of a double $d_Q$ sum, tested against $\varepsilon(j+2, \beta)$.
- `QLast`: the same kind of identity at the last step, with integrals over a fundamental domain of the top group and with $\varepsilon_T$.
- `QFin`: there are a compact open subgroup $K_1$ and a finite set $T_1$ at the places of $Q$ such that $K_1$ acts on the vacuum vectors by scalars $a^{-1}$ and $a$, and each $x$ with a nonzero term for $g$ in the support of $\varepsilon(j, \alpha)$ lies in $r\,T_1 K_1$, with $r$ in a Jacquet type subgroup.

We have not unfolded `Iter2`, `per`, `Vac` or `flatBF`.

**Theorem.** If $c$, $t$ and $v$ satisfy `Is`, $v$ satisfies `WeilOK` for $t$, and `QPinU v w`, then `QLaw v w`, `QLast v w` and `QFin v w` hold.

## Proof

1. For a pinned tuple $w_0$, three lemmas give the laws: `seeSawIteratedIntegralLaw_at_twist_of_factorisation` gives `QLaw`, `seeSawIteratedIntegralLawLastSteps_of_localFactorisation` gives `QLast`, and `seeSawFiniteCells_at_twistPlaces_of_localFactorisation` gives `QFin`. Each one is a restatement of a lemma in another file; we have not opened those proofs.
2. `RescTest.laws_of_qpinU` moves the laws from $w_0$ to $\mathrm{resc}(w_0, s)$. It applies step 1 to `free w₀`, which is $w_0$ with $F_X$ replaced by all functions. This tuple is still pinned (`qpin_free`), because the pin does not involve $F_X$.
3. For `QLaw` and `QLast` (lemmas `qlaw_resc` and `qlast_resc`), apply the law for `free w₀` to the test family $s_j(\alpha)\varphi_\alpha$. The lemma `inner` pulls the factor $s_{j+2}(\beta)^{-1}$ out of the double $d_Q$ sum. The rescaled $\varepsilon$ at level $j+2$ gives the factor $s_{j+2}(\beta)$. The two factors cancel. This needs only $s_j(\alpha) \neq 0$, which follows from $s_j(\alpha)^n = 1$ (`root_ne`).
4. For `QFin` (`qfin_resc`), the support of $s \cdot \varepsilon$ lies in the support of $\varepsilon$, and the other data in `QFin` do not change. This needs nothing on $s$.

## In the Lean code

The theorem is at [SeeSawTwistPlaceLawsOfRootOfUnityRescaling.lean](lean:Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/SeeSawTwistPlaceLawsOfRootOfUnityRescaling.lean#L15). The proof is one term, `RescTest.laws_of_qpinU v (fun w₀ h₀ => ⟨…, …, …⟩) w h`, with the three lemmas of step 1. The definitions are in [RescOne.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/RescOne.lean#L9) (`resc`, `QPinU`), [CosInj.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CosInj.lean#L152) (`QPin`) and [PlaceLaws.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/PlaceLaws.lean#L228) (`QLaw`, `QLast`, `QFin`). The rescaling lemmas are in [CombSmulLeft.lean](lean:Development/AbelianVarietyTheory/Definitions/LatticeFrames/CombSmulLeft.lean#L165).

The root of unity condition is stronger than the proof needs: nonzero scalars suffice. Only `norm_dQ` (line 181 of the same file) uses $|s_j(\alpha)| = 1$, and `laws_of_qpinU` does not call it.
