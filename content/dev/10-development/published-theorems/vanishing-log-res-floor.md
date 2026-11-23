---
id: vanishing-log-res-floor
title: Vanishing on a log resolution for the rounded-down divisor
kind: theorem
decl: GlobalTheory.Discrepancy.vanishing_logRes_floor
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.MultiplierVanishingNefTwist
covers: 607
status: drafted
drafted_by: writer@claude
---
This theorem proves the vanishing on the log resolution $Y$ that [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/) pushes down to $X$. It reaches that theorem through its second name [`multiplier_vanishing_nef_twist`](/entry/multiplier-vanishing-nef-twist/). The proof reduces it to a Kawamata-Viehweg vanishing on $Y$, [`snc_boundary_ample_decomposition`](/entry/snc-boundary-ample-decomposition/).

## Statement

We use the hypotheses and the names of [`vanishing_logRes_pushforward_and_local`](/entry/vanishing-log-res-pushforward-and-local/): $s \colon Y \to X$ is a log resolution with canonical divisor $K = \operatorname{div}(s^*\eta)$ and boundary $B$; $F$ has multiplicities $\lfloor (s^*G - mK)/m \rfloor$; $T = mr\,N - r\,G - m\,M$ in $\operatorname{Pic} X$ with $M$, $T$ nef; $a\,s^*M = A + F_d$ with $A$ ample and $F_d \geq 0$ supported in $B$.

**Theorem.** For each line bundle $Q$ on $Y$ with $Q = s^*N - F$ in $\operatorname{Pic} Y$, $H^i(Y, Q) = 0$ for all $i > 0$.

In other words, $H^i\bigl(Y, \mathcal{O}_Y(K + s^*N - \lfloor s^*G/m \rfloor)\bigr) = 0$ for $i > 0$, where $s^*N - \tfrac1m s^*G$ is nef and big. This is the vanishing on a log resolution in the usual proof of Nadel vanishing (Lazarsfeld, *Positivity in Algebraic Geometry II*, Section 9.4).

## Proof

Let $\Gamma = s^*G - mK$ and $R = \Gamma - mF$.

1. **The remainder.** At each point, $R$ has multiplicity $\Gamma \bmod m$, so $0 \leq R < m$. So $R$ is effective (`cartier_divisor_mult_characterize`), and its support is in that of $\Gamma$, so in $B$.
2. **A boundary below the threshold.** `exists_multiple_below_threshold` gives $b \geq a$ such that $\Gamma' = rb\,R + m\,F_d$ has all multiplicities $< mrb$. $\Gamma'$ is effective with support in $B$.
3. **An ample bundle.** The pullbacks $s^*T$ and $s^*M$ are nef (`nef_pullback_is_nef`). So $P = b\,s^*T + m(b-a)\,s^*M$ is nef, and $A' = mA + P$ is ample (`ample_add_nef_is_ample`).
4. **The canonical class.** `canonical_divisor_of_form` says that $K$ is in the class of the canonical bundle $\omega_Y$. It needs $s^*\eta \neq 0$, which holds since $s$ is birational (`rationalTopFormPullback_bijective_birational`).
5. **Kawamata-Viehweg.** With $e = mrb$, the relations of the hypotheses give $e\,Q = e\,K + \Gamma' + A'$ in $\operatorname{Pic} Y$. Then [`snc_boundary_ample_decomposition`](/entry/snc-boundary-ample-decomposition/) gives $H^i(Y, Q) = 0$ for $i > 0$. In rational terms, $Q = K + \tfrac1e \Gamma' + \tfrac1e A'$, with $\tfrac1e \Gamma'$ an SNC boundary with coefficients in $[0, 1)$ and $\tfrac1e A'$ ample.

The check of the relation in step 5 is a computation in $\operatorname{Pic} Y$ (`module`).

## In the Lean code

The theorem is in [MultiplierVanishingNefTwist.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwist.lean#L69). The lemmas it calls, all of the form `GlobalTheory.T.<name>`:

- `snc_boundary_ample_decomposition`, the vanishing theorem;
- `exists_multiple_below_threshold`, `cartier_divisor_mult_characterize`;
- `nef_pullback_is_nef`, `ample_add_nef_is_ample`;
- `canonical_divisor_of_form`, `rationalTopFormPullback_bijective_birational`.

The quotient $/m$ in the hypothesis on $F$ is division in $\mathbb{Z}$. The proof uses `Int.emod_def`, so it is the floor for $m > 0$.

The hypothesis $a > 0$ is never used: the proof unpacks it and drops it. The proof only needs $b \geq a$, for any $a$.
