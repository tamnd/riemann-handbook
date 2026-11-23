---
title: Nadel vanishing on a log resolution
decls:
  - GlobalTheory.Discrepancy.vanishing_logRes_floor
  - GlobalTheory.T.multiplier_vanishing_nef_twist
  - GlobalTheory.vanishing_logRes_pushforward_and_local
  - GlobalTheory.T.multiplier_vanishing_nef_twist_ample
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Nadel vanishing on a log resolution

This section proves the two vanishing theorems for [multiplier ideals](/learn/positivity-resolution/#multiplier-ideals-and-nadel-vanishing) ([[multiplier ideal|BKM0TQSCD9]]) in the form that the rest of the proof uses: Nadel vanishing on $X$ and local vanishing on a log resolution ([Theorem 9.6.3](/entry/vanishing-log-res-pushforward-and-local/)). Both follow from Kawamata-Viehweg vanishing on the resolution, in the form of Section 5. The variety $X$ is not assumed to be smooth. The divisor that is rounded down is $\frac1m$ times an integral divisor, and the positivity is given by integral relations in $\operatorname{Pic}$, so that no $\mathbb{Q}$-divisors occur in the statements.

Let $k$ be a field of characteristic $0$ and $X$ an integral scheme, projective over $k$, with function field $K(X)$. A *rational $n$-form* on $X$ is an element of $\bigwedge^n_{K(X)} \Omega_{K(X)/k}$. If $Y$ is smooth of relative dimension $n$ over $k$ and $\eta$ is a nonzero rational $n$-form on $Y$, the *divisor of $\eta$* is the Cartier divisor whose local equation at $y$ is the $g \in K(Y)^\times$ with $\eta = g\,\omega$ for $\omega$ a free generator of $\Omega^n_Y$ near $y$. Its class in $\operatorname{Pic} Y$ is the class of the canonical bundle, so it is a [canonical divisor](/learn/geometry/#line-bundles-and-divisors) ([[canonical divisor|W05VYY4HBR]]).

**Definition 9.6.1 (Log resolution of a form and a divisor).** Let $\eta \neq 0$ be a rational $n$-form on $X$, $G$ a Cartier divisor on $X$ and $m > 0$ an integer. A *log resolution* of $(\eta, m, G)$ is a dominant morphism $s : Y \to X$ of integral schemes, a Cartier divisor $K$ on $Y$ and a closed set $B \subseteq Y$ such that:

1. $Y$ is smooth of relative dimension $n$ and projective over $k$;
2. $s$ is birational, that is, $s^* : K(X) \to K(Y)$ is bijective;
3. $K$ is the divisor of the pullback $s^*\eta$;
4. $B$ is a divisor with simple normal crossings, in the sense of Section 5;
5. the support of $s^*G - mK$ is contained in $B$.

Such a resolution exists by [resolution of singularities](/learn/positivity-resolution/#resolution-of-singularities-and-principalization) (Hironaka). When $X$ is smooth and $K_X$ is the divisor of $\eta$, then $K = s^*K_X + K_{Y/X}$, with $K_{Y/X}$ the relative canonical divisor.

A line bundle $T$ on $X$ is *[nef](/learn/positivity-resolution/#ample-nef-and-big-line-bundles)* ([[nef|RZ66X0NAM5]]) if $\deg(T|_C) \geq 0$ for every complete integral curve $C \subseteq X$. Ample bundles are nef, the pullback of a nef bundle along a morphism of projective varieties is nef, a tensor product of nef bundles is nef, and an ample bundle tensored with a nef bundle is ample.

In the rest of the section we fix the following data, and call it the *Nadel setting*. Let $(s : Y \to X, K, B)$ be a log resolution of $(\eta, m, G)$. Let $F$ be the Cartier divisor on $Y$ with
$$\operatorname{mult}_z F = \Big\lfloor \frac{\operatorname{mult}_z(s^*G - mK)}{m} \Big\rfloor \quad \text{for all } z.$$
Let $N$, $M$ and $T$ be line bundles on $X$, with $M$ and $T$ nef, and $r > 0$ an integer, such that
$$[T] = mr[N] - r[\mathcal{O}_X(G)] - m[M] \quad \text{in } \operatorname{Pic} X.$$
Let $a$ be an integer, $F_d$ an effective Cartier divisor on $Y$ with support in $B$, and $A$ an ample line bundle on $Y$, such that $a\, s^*[M] = [A] + [\mathcal{O}_Y(F_d)]$ in $\operatorname{Pic} Y$.

In rational terms: put $D = \frac1m G$. Since $K$ is integral, $F = \lfloor s^*D \rfloor - K$. The relation says $N - D \equiv \frac1r M + \frac1{mr} T$, and the last condition says that $s^*M$ is big, with a decomposition into an ample and an effective part supported on $B$. So $N - D$ is nef and big.

**Theorem 9.6.2 (Vanishing on the resolution).** In the Nadel setting, let $Q$ be a line bundle on $Y$ with $[Q] = s^*[N] - [\mathcal{O}_Y(F)]$. Then $H^i(Y, Q) = 0$ for all $i > 0$.

Lean: `GlobalTheory.Discrepancy.vanishing_logRes_floor` (also `GlobalTheory.T.multiplier_vanishing_nef_twist`, a second name).

In rational terms, $Q = K + s^*N - \lfloor s^*D \rfloor$, and the theorem is Kawamata-Viehweg vanishing on $Y$ for the nef and big class $s^*(N - D)$, with the round down of an snc divisor.

*Proof.* $Y$ is normal, since it is smooth over $k$, and quasi-compact, since it is projective. Put $\Gamma = s^*G - mK$ and $R = \Gamma - mF$.

Step 1 (the fractional part). For each $z$, $\operatorname{mult}_z R = \operatorname{mult}_z \Gamma - m\lfloor \operatorname{mult}_z \Gamma / m \rfloor$ is the remainder of $\operatorname{mult}_z \Gamma$ modulo $m$, so $0 \leq \operatorname{mult}_z R < m$. Since $Y$ is normal, $R$ is effective. If $z$ is in the support of $R$, then $\operatorname{mult}_z \Gamma \neq 0$, so $z$ is in the support of $\Gamma$, which lies in $B$. So the support of $R$ lies in $B$.

Step 2 (a large multiple). Since $\operatorname{mult}_z R \leq m - 1$ and $F_d$ has finitely many components, there is an integer $b \geq a$ such that the divisor
$$\Gamma' = rb\,R + m F_d$$
has $\operatorname{mult}_z \Gamma' < mrb$ for all $z$. Indeed $\operatorname{mult}_z \Gamma' \leq rb(m-1) + m \operatorname{mult}_z F_d$, and this is $< mrb$ as soon as $rb > m \max_z \operatorname{mult}_z F_d$. $\Gamma'$ is effective with support in $B$, by Step 1.

Step 3 (the ample part). The bundles $s^*T$ and $s^*M$ are nef on $Y$. Let $P$ be a line bundle with $[P] = b\, s^*[T] + m(b - a)\, s^*[M]$; it is nef, as $b - a \geq 0$. Let $A'$ be a line bundle with $[A'] = m[A] + [P]$. Then $A'$ is ample, as $A^{\otimes m}$ is ample and $P$ is nef.

Step 4 (the canonical class). As $s$ is birational, $s^*\eta \neq 0$, so its divisor $K$ has the class $[\omega_Y]$ of the canonical bundle $\omega_Y$ of $Y$.

Step 5 (the relation). Put $e = mrb$. We check
$$e[Q] = e[\omega_Y] + [\mathcal{O}_Y(\Gamma')] + [A'].$$
Write all classes additively on $Y$ and drop the $s^*$. The right side is $mrbK + rb(\Gamma - mF) + mF_d + mA + bT + m(b-a)M$. Substitute $\Gamma = G - mK$, $mF_d + mA = maM$ and $bT = mrbN - rbG - mbM$. The terms in $K$, $G$ and $M$ cancel, and the right side is $mrbN - mrbF = e[Q]$.

Step 6. Now $Y$ is smooth of relative dimension $n$ and projective over $k$, $B$ has simple normal crossings, $\Gamma'$ is effective with support in $B$ and multiplicities $< e$, and $A'$ is ample. So [Theorem 9.5.2](/entry/vanishing-ample-snc-cartier/) gives $H^i(Y, Q) = 0$ for $i > 0$. $\square$

**Theorem 9.6.3 (Nadel vanishing and local vanishing).** In the Nadel setting:

1. $H^i\big(X, s_*\mathcal{O}_Y(-F) \otimes N\big) = 0$ for all $i > 0$;
2. for each affine open $U \subseteq X$ and each $j > 0$, $H^j\big(s^{-1}U, \mathcal{O}_Y(-F) \otimes s^*N\big) = 0$.

Lean: `GlobalTheory.vanishing_logRes_pushforward_and_local` (also `GlobalTheory.T.multiplier_vanishing_nef_twist_ample`, a second name).

When $X$ is smooth and $K_X$ is the divisor of $\eta$, then $\mathcal{O}_Y(-F) = \mathcal{O}_Y(s^*K_X + K_{Y/X} - \lfloor s^*D \rfloor)$, so by the projection formula $s_*\mathcal{O}_Y(-F) = \mathcal{O}_X(K_X) \otimes \mathcal{J}(D)$, with $\mathcal{J}(D)$ the multiplier ideal. Then part 1 is Nadel vanishing $H^i(X, \mathcal{O}_X(K_X + N) \otimes \mathcal{J}(D)) = 0$ for $N - D$ nef and big (Nadel, Ann. of Math. 132, 1990; Lazarsfeld, *Positivity* II, Theorem 9.4.8), and part 2 is local vanishing, $R^j s_*\mathcal{O}_Y(K_{Y/X} - \lfloor s^*D \rfloor) = 0$ for $j > 0$ (*Positivity* II, Theorem 9.4.1).

*Proof.* $X$ and $Y$ are projective over $k$, so they are separated and quasi-compact. Let $H$ be an ample line bundle on $X$.

Step 1 (all admissible twists). Let $N'$ and $T'$ be line bundles on $X$, with $T'$ nef and $[T'] = mr[N'] - r[\mathcal{O}_X(G)] - m[M]$. Choose $Q'$ with $[Q'] = s^*[N'] - [\mathcal{O}_Y(F)]$. Then $Q' \cong \mathcal{O}_Y(-F) \otimes s^*N'$, and the last theorem, with $N'$ and $T'$ in place of $N$ and $T$, gives $H^i(Y, \mathcal{O}_Y(-F) \otimes s^*N') = 0$ for $i > 0$.

Step 2 (twists by $H$). For $c \geq 0$ put $N_c = N \otimes H^{\otimes c}$ and $T_c = T \otimes H^{\otimes mrc}$. Then $T_c$ is nef, as $H$ is ample, hence nef, and $[T_c] = mr[N_c] - r[\mathcal{O}_X(G)] - m[M]$. So Step 1 gives
$$H^j\big(Y, \mathcal{O}_Y(-F) \otimes s^*N \otimes s^*H^{\otimes c}\big) = 0 \quad \text{for all } j > 0 \text{ and all } c \geq 0.$$

Step 3 (the higher direct images). Let $\mathcal{F} = \mathcal{O}_Y(-F) \otimes s^*N$, a quasi-coherent sheaf on $Y$. A lemma on direct images says: if $H$ is ample on $X$ and $H^j(Y, \mathcal{F} \otimes s^*H^{\otimes c}) = 0$ for $j > 0$ and all large $c$, then $H^j(s^{-1}U, \mathcal{F}) = 0$ for $U$ affine and $j > 0$, and $H^i(X, s_*\mathcal{F}) \cong H^i(Y, \mathcal{F})$ for all $i$. This is the argument of Lazarsfeld (*Positivity* I, Lemma 4.3.10): by the projection formula and the Leray spectral sequence, for $c$ large $H^0(X, R^j s_*\mathcal{F} \otimes H^{\otimes c}) = H^j(Y, \mathcal{F} \otimes s^*H^{\otimes c}) = 0$, while $R^j s_*\mathcal{F} \otimes H^{\otimes c}$ is globally generated, so $R^j s_*\mathcal{F} = 0$. By Step 2 the hypothesis holds, and this gives part 2.

Step 4 (part 1). By the projection formula, $s_*\mathcal{F} \cong s_*\mathcal{O}_Y(-F) \otimes N$. So by Step 3 and Step 1 with $N' = N$ and $T' = T$,
$$H^i\big(X, s_*\mathcal{O}_Y(-F) \otimes N\big) \cong H^i(Y, \mathcal{F}) = 0 \quad \text{for } i > 0. \qquad \square$$

**Remark 9.6.4 (Formalization).** The floor $\lfloor \cdot / m \rfloor$ is the integer division `/` on `ℤ`, which is the floor since $m > 0$. In [MultiplierVanishingNefTwist.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwist.lean#L71) the hypothesis `0 < a` is taken apart into `ha` and not used: the proof needs only $b \geq a$. In [MultiplierVanishingNefTwistAmple.lean](lean:Development/WeilBound/CoreStatements/PublishedTheorems/NadelVanishingPairs/NadelVanishingLemmas/MultiplierVanishingNefTwistAmple.lean#L46) the eventual vanishing `hev` is proved for every $c$ by `Eventually.of_forall`, as in Step 2. Step 2 of the first proof is `GlobalTheory.T.exists_multiple_below_threshold`, Step 3 of the second is `GlobalTheory.T.pushforward_cohomology_affine`, and Step 4 of the first is `GlobalTheory.T.canonical_divisor_of_form` with `GlobalTheory.T.rationalTopFormPullback_bijective_birational`; we read their statements only. Nef means `IsNef`: degree $\geq 0$ on each complete integral curve, through an intersection number on the reduced curve. The second names `GlobalTheory.T.multiplier_vanishing_nef_twist` and `GlobalTheory.T.multiplier_vanishing_nef_twist_ample` are proved by `first | exact @… | …`; their statements do not contain a multiplier ideal, only the divisor $F$. The relation of $s_*\mathcal{O}_Y(-F)$ to $\mathcal{J}(D)$ is not stated in these files.
