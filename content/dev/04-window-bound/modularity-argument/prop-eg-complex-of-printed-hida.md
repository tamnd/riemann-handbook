---
id: prop-eg-complex-of-printed-hida
title: Eisenstein-congruent Galois representations from Eisenstein-congruent eigenforms
kind: theorem
decl: UpperTheory.V.Z.Sym.W.prop_eg_complex_of_printed_hida
module: Development.AutomorphicArithmetic.AutomorphicVarieties.ModularityArgument.ThresholdArguments.DenseThresholdCases.WEGCore
covers: 750
status: drafted
drafted_by: writer@claude
---
This theorem proves `PropEGc` from the published hypotheses `HypothesesH'`: there are 2-dimensional Galois representations congruent to a sum of two characters, with control of their Frobenius eigenvalues. Its result goes to [`prop_eg_w_of_printed_hida`](/entry/prop-eg-w-of-printed-hida/), which turns the eigenvalue control into an unlinked adjoint. The proof finds an eigenform that is congruent to an Eisenstein series and passes it to [`core`](/entry/eg-core/).

## Statement

Let $\ell$ be a prime, $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$, $c$ a complex conjugation and $\varepsilon$ the cyclotomic character. Let $N, w$ and characters $\varphi, \theta$ of $G_{\mathbb{Q}}$ satisfy:

- `SlopeTestRemainingChoices N w θ`: $\ell \ne 2$, $N > 0$, $\ell \nmid N$, $w$ is a prime with $w \nmid N$, $\theta \ne 1$, $\theta^\ell = 1$, and $\theta$ is trivial on the elements that fix the $w$-th roots of unity (`KillsMu`);
- `SplitAt N w φ`: $\varphi$ kills the elements that fix the $N$-th roots of unity, and $\varphi(s) = 1$ when $s$ acts on them as $\zeta \mapsto \zeta^w$;
- $\varphi \ne 1$.

**Theorem.** Assume `HypothesesH'`. Then there is $k_0$ such that for each $k \ge k_0$ with $\varphi(c) = (-1)^k$ there is a continuous $\rho \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ with these properties.

- `EisRep ι φ θ k ρ`: $\rho$ is irreducible and modular (`IsAutR`), $\det \rho = \varepsilon^{k-1}\varphi\theta$, the characteristic polynomials of $\rho$ are congruent to those of $1 \oplus \varepsilon^{k-1}\varphi$ (`ResSum`), the type away from $\ell$ is given by $1$ and $\varphi\theta$, and $\rho$ is ordinary above $\ell$ with weights $k - 1, 0$ and characters $\varepsilon^{k-1}\varphi, 1$.
- `PR`: $\rho$ is attached to a regular algebraic cuspidal $\pi$ with the condition `PlainR`.
- `RW`: at each Frobenius at $v \nmid \ell$, any two eigenvalues satisfy $|\iota\alpha| < N(v)\,|\iota\beta|$.
- `NoHalf`: at the same Frobenius, $|\iota\alpha|^2 \ne N(v)\,|\iota\beta|^2$.

## Proof

1. **Dirichlet characters.** `dirOf` writes $\varphi$ as the Galois character of a primitive Dirichlet character $\varphi_0$ of conductor $M \mid N$. It writes $\theta$ as that of a character $\theta_0$ mod $w$. Let $\chi = \varphi_0\theta_0$ mod $Mw$ (`exists_mul`).
2. **The data `EDat`.** The proof checks $M > 1$ (as $\varphi \ne 1$), $\theta_0 \ne 1$ and $\theta_0^\ell = 1$, so $\theta_0$ has order $\ell$ and $\ell \mid w - 1$. `SplitAt` gives $\varphi_0(w) = 1$. Then $\ell \nmid Mw$.
3. **Eigenform.** `propEC` gives $k_0$. For $k \ge k_0$ with $\varphi_0(-1) = (-1)^k$ there is an eigenform $g$ of weight $k$, level $Mw$ and character $\chi$, with the condition `Cj`, such that $a_p(g) \equiv 1 + \chi(p)p^{k-1}$ modulo the maximal ideal for each prime $p$.
4. **Galois side.** Take $k \ge \max(k_0, 3)$. The private lemma `core` turns $g$ into $\rho$. It uses `ordExT_sv_alt` to get an ordinary representation $r$ attached to $g$, and sets $\rho$ to be the twist of $r$ by $D = \varepsilon^{k-1}\varphi\theta$. Then it proves `EisRep` field by field, `PR` by `prTw` and `prOrd`, `RW` by `ordWin_a_alt`, and `NoHalf` by [`half_of_printed_hida`](/entry/half-of-printed-hida/). The twist keeps `RW` and `NoHalf` by `twOk`.
5. The last step checks that the Galois character of $\chi$ is $\varphi\theta$. The rest is bookkeeping.

## In the Lean code

The theorem is in [WEGCore.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WEGCore.lean#L235), and `core` is in the same file at line 129. The lemmas:

- `PropEGc` in [EGCore.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/WeilDeligneUnramified/EGCore.lean#L265);
- `propEC` in [PropEC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnlinkedHeckeRoots/PropEC.lean#L191), with its statement in [UnitFormC.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/SymmetricPowerTransfer/UnlinkedHalfIntegral/UnitFormC.lean#L49);
- `ordExT_sv_alt` in [SVOrdExT.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/SVOrdExT.lean#L52);
- `EisRep` and `SlopeTestRemainingChoices` in [SlopeTestRemainingChoices.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/IdeleGenerators/SlopeTestRemainingChoices.lean#L101).

`HypothesesH'` is used only inside `core`. The lemma `core` is private, so its outline entry [`eg-core`](/entry/eg-core/) is for a name that other files cannot call.
