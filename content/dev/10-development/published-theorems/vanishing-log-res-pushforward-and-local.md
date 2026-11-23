---
id: vanishing-log-res-pushforward-and-local
title: Nadel vanishing and local vanishing on a log resolution
kind: theorem
decl: GlobalTheory.vanishing_logRes_pushforward_and_local
module: Development.WeilBound.CoreStatements.PublishedTheorems.NadelVanishingPairs.NadelVanishingLemmas.MultiplierVanishingNefTwistAmple
covers: 701
status: drafted
drafted_by: writer@claude
---
This theorem pushes a vanishing theorem on a log resolution $Y \to X$ down to $X$: the higher cohomology of a multiplier-type sheaf on $X$ vanishes, and so do the higher direct images. Its only user is the second name [`multiplier_vanishing_nef_twist_ample`](/entry/multiplier-vanishing-nef-twist-ample/). The vanishing on $Y$ comes from [`multiplier_vanishing_nef_twist`](/entry/multiplier-vanishing-nef-twist/).

## Statement

Let $k$ be a field of characteristic $0$. The hypotheses are:

- $X$ is an integral scheme, projective over $k$; $\eta \neq 0$ is a rational $n$-form on $X$; $m > 0$; $G$ is a Cartier divisor on $X$.
- $s \colon Y \to X$ is a log resolution (`IsLogRes`): $Y$ is integral, smooth of relative dimension $n$ and projective over $k$; $s$ is dominant and birational; $K$ is the divisor of $s^*\eta$, so a canonical divisor of $Y$; $B \subseteq Y$ is closed and satisfies `Snc`, by its name a simple normal crossing condition; $s^*G - mK$ has support in $B$.
- $F$ is the Cartier divisor on $Y$ with multiplicities $\lfloor (s^*G - mK)/m \rfloor$. So $F = \lfloor s^*G/m \rfloor - K$.
- $N$, $M$, $T$ are line bundles on $X$, with $M$ and $T$ nef (degree $\geq 0$ on each complete curve), $r > 0$, and $T = mr\,N - r\,G - m\,M$ in $\operatorname{Pic} X$. With rational coefficients, $N = \tfrac1m G + \tfrac1r M + \tfrac1{mr} T$.
- $a > 0$, $F_d$ is an effective Cartier divisor on $Y$ with support in $B$, and $A$ is an ample line bundle on $Y$ with $a\,s^*M = A + F_d$ in $\operatorname{Pic} Y$. So $s^*M$ is big.

**Theorem.** Under these hypotheses:

1. $H^i\bigl(X, s_*\mathcal{O}_Y(-F) \otimes N\bigr) = 0$ for all $i > 0$;
2. for each affine open $U \subseteq X$ and each $j > 0$, $H^j\bigl(s^{-1}U, \mathcal{O}_Y(-F) \otimes s^*N\bigr) = 0$. That is, the higher direct images of $\mathcal{O}_Y(-F) \otimes s^*N$ vanish.

Here $\mathcal{O}_Y(-F) = \mathcal{O}_Y(K - \lfloor s^*G/m \rfloor)$. If $X$ is smooth and $K_X = \operatorname{div}\eta$, then $s_*\mathcal{O}_Y(-F) = \mathcal{O}_X(K_X) \otimes \mathcal{J}(\tfrac1m G)$, with $\mathcal{J}$ the multiplier ideal. Then part 1 is Nadel vanishing for $K_X + N$ with $N - \tfrac1m G$ nef and big, and part 2 is local vanishing (Lazarsfeld, *Positivity in Algebraic Geometry II*, Section 9.4). The Lean statement does not ask $X$ to be smooth.

## Proof

1. **Vanishing on $Y$ for all admissible $N'$.** Let $N'$, $T'$ satisfy the hypotheses of $N$, $T$. Take $Q$ with class $s^*N' - F$ (`cls_surj`). Then [`multiplier_vanishing_nef_twist`](/entry/multiplier-vanishing-nef-twist/) gives $H^i(Y, Q) = 0$ for $i > 0$. As $Q \cong \mathcal{O}_Y(-F) \otimes s^*N'$ (`nonempty_twist_twist_iso_of_cls_eq`), $H^i(Y, \mathcal{O}_Y(-F) \otimes s^*N') = 0$.
2. **Twists by an ample bundle.** Let $H$ be ample on $X$ (`exists_isAmpleLB_of_isProjOver`). For each $c$, the pair $N \otimes H^c$, $T \otimes H^{mrc}$ satisfies the hypotheses: $H$ is nef, and a product of nef bundles is nef. So by step 1, $H^j(Y, \mathcal{O}_Y(-F) \otimes s^*N \otimes s^*H^c) = 0$ for all $j > 0$ and $c$.
3. **Leray.** `pushforward_cohomology_affine` takes this vanishing for large $c$. It gives part 2, and $H^i(X, s_*\mathcal{E}) \cong H^i(Y, \mathcal{E})$ for $\mathcal{E} = \mathcal{O}_Y(-F) \otimes s^*N$.
4. The projection formula $s_*\mathcal{E} \cong s_*\mathcal{O}_Y(-F) \otimes N$ (`Twist.projIso`) and step 1 for $N$ itself give part 1.

## In the Lean code

The theorem is in [MultiplierVanishingNefTwistAmple.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwistAmple.lean#L25). The lemmas it calls:

- `GlobalTheory.T.multiplier_vanishing_nef_twist`, a second name of [`vanishing_logRes_floor`](/entry/vanishing-log-res-floor/);
- `GlobalTheory.T.pushforward_cohomology_affine`;
- `exists_isAmpleLB_of_isProjOver`, `isSeparated_of_isProjOver` (same file), `cls_surj`, `nonempty_twist_twist_iso_of_cls_eq`, `Twist.projIso`.

The hypotheses $\eta$, $m$, $G$, $K$, $B$, $a$, $F_d$, $A$ and $M$ are passed to step 1 with no change. The reading as Nadel vanishing is ours; the Lean code does not name it.
