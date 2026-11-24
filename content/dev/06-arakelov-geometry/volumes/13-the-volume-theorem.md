---
title: The volume theorem
decls:
  - GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs
  - GlobalTheory.T.volume_theorem_of_inputs
  - GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume
  - GlobalTheory.T.good_tower_volume_theorem
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The volume theorem

This section proves the main theorem of the chapter. Every good root tower over a global integral model is proportional, has equal volumes on its components, and satisfies the limit formula T1, Theorem B, the lower bound T2 and the mean slope bound, with one constant $C$ for all towers. Together with the existence of good root towers, this is the volume part of Step 4 of [the Weil bound](/proof/weil-bound/). The proof checks, for a good tower, each hypothesis of [the chain of tower estimates](/entry/chain-tower/), using the results of the previous sections and of the chapters on heights and on good towers.

We keep the notation of [the tower conditions](/entry/full-intersection-tower-i8-identity/). For a CM field $E$ with host $H$ we write $\mathrm{rd}_E$ for the root discriminant and $L_H$ for the value $L'(1, \chi)/L(1, \chi)$ of the quadratic character of the host, and

$$
\Lambda_B = \log(B\, \mathrm{rd}_E) + |L_H|.
$$

The bracket $\beta_B(u)$ of T2 and of the mean slope bound is formed with this $\Lambda_B$.

**Definition 9.13.1 (The volume statement).** The volume statement says: there is $C \ge 0$ such that for every CM field $E$ abelian over $\mathbb{Q}$, with host $H$, every datum $D$ of signature $(p, q)$, every family $X_o$ of moduli spaces, every level $l$, coefficient field $c$ and integral model $Y$ of $X_o(l)$, every root tower $T$ of type $(\Psi, p + q)$ with a good origin $o$ over $Y$, and every intersection system $\mathrm{II}$, if

1. $Y$ is global, $o$ satisfies the extra conditions and $\mathrm{II}$ is full,
2. $q \ge 1$ and $3q + 1 \le p + q$,
3. $T$ has at most $4|\Psi|(p + q)^2$ bad primes,

then $T$ is proportional, has equal volumes, satisfies T1, satisfies Theorem B for the arithmetic flag height, and satisfies T2 and the mean slope bound with the constant $C$, the root discriminant $\mathrm{rd}_E$ and the value $L_H$.

**Definition 9.13.2 (The existence statement).** The existence statement says: for every CM field $E$ with host $H$, datum $D$ with $p, q \ge 1$, family $X_o$, level $l$, coefficient field $c$ and integral model $Y$ of $X_o(l)$ that is global and has split components, there are a root tower $T$ of type $(\Psi, p + q)$ and a good origin of $T$ over $Y$ that satisfies the extra conditions.

The volume statement is proved from ten inputs: the top level inputs; the integrability of points; the Weil pairing statement; the existence of constants $C_h$, $C_u$ for the geometric height bound of the chapter on good towers; the Hodge lattice flag bound; the trivial flag statement on Hodge components; the flat degree statement of [the section on constant sections](/entry/flat-degree-st-of-res-k-gaga/); the twist statement on automorphisms; the comparison statement for pairs of root models; and the comparison input.

**Theorem 9.13.3 (Volume theorem from its inputs).** The ten inputs imply the volume statement, with the constant

$$
C = 2\max\big(C_h + \tfrac{C_u}{2}, 0\big) + 17.
$$

Lean: `GlobalTheory.CompanionTheory.Ar.Cusp.volumeTheoremX_of_inputs` (also `GlobalTheory.T.volume_theorem_of_inputs`, a second name)

*Proof.* Put $C_0 = \max(C_h + C_u/2, 0)$. Let the data be given. The host numbers give $\mathrm{rd}_E \ge 2$, so $\mathrm{rd}_E \ge 1$, and that $\Psi$ is nonempty. From $3q + 1 \le p + q$ we get $p \ge 1$ and $q \le p$. We check the hypotheses of the chain of tower estimates one by one.

1. Proportionality. The agreement statement for the real tower of a good origin, with the proved positivity of agreement, gives a real tower over $T$; the proportionality of real towers then gives that $T$ is proportional.
2. Convergence, I2 and I1. The convergence statement for real towers gives the limits $\mathrm{PP}_{B, c}$ and I2. The bound I1 follows from the real tower bound applied to the reference link of [the section on reference towers](/entry/level/).
3. A1. The real tower satisfies A1, since the origin is smooth, flat and positive on every component.
4. Nefness. M1 and M2 hold for good towers at small, bad and large primes. The ample line is nef on the fibres, since its degree vector has a single entry $1$. The general nefness of real towers with the nef polarization statement, and the real conditions of good towers, give I7.
5. I5 and I6. These are the [height bounds for points](/entry/global-model-tower-fifth-condition/).
6. I8. This is the [antisymmetry theorem](/entry/full-intersection-tower-i8-identity/), with the comparison input and the Weil pairing statement.
7. Proposition 6 and the Frobenius shape. The theorem on [good towers being linked](/entry/good-origin-linked/) gives labels $\varphi$ whose label map has Frobenius shape and a link of $T$; the power sum theorem for linked towers gives Proposition 6.
8. Proposition A. The symmetry statement for good towers with global extra conditions, with the twist statement and the comparison statement for pairs.
9. Proposition F with constant $4$. The top level form of Proposition F, with the integrability of points, the convergence, proportionality, Proposition 6, $\mathrm{rd}_E \ge 1$, the fact that the bad primes are prime, and the [flat root lines of near record height](/entry/root-flat-on-hodge/).
10. Equal volumes. This is the theorem of [the previous section](/entry/vol-eq-of-is-full-intersection-system/).
11. The slope lower bound. The index $j$ of the tower is $p$, so $3(N - j) + 1 \le N$. The slope lower bound for base settings, with the base settings of good towers built from the geometric height constants, gives the slope lower bound with constant $C_h + C_u/2$. Raising the constant to $C_0 \ge C_h + C_u/2$ keeps the bound, since the term it multiplies is nonnegative for $B \ge 128$ and $\mathrm{rd}_E \ge 1$.

The chain of tower estimates, with the flag height statement, the inputs of the proof theory, the two successive minima bounds, the antisymmetric perturbation statement, the height bound for Grassmannians, the constants $C_0$ and $4$, and the eleven items above, gives T1, Theorem B, T2 and the mean slope bound, with the constant $2C_0 + 3 \cdot 4 + 5 = C$. With items 1 and 10 this is the volume statement. $\square$

The raising step uses that the volumes are positive, so the total volume is nonnegative, and that $\Lambda_B \ge 0$ for $B \ge 128$ and $\mathrm{rd}_E \ge 1$.

**Theorem 9.13.4 (Good towers and the volume theorem).** Assume the top level inputs, the integrability of points, the prime avoidance statement, the Weil pairing statement, the existence of local lattice families at good primes, and the comparison statement for pairs of root models. Then the existence statement and the volume statement hold.

Lean: `GlobalTheory.CompanionTheory.Ar.Top.goodTower_and_volume` (also `GlobalTheory.T.good_tower_volume_theorem`, a second name)

*Proof.* The two parts are independent.

For the existence statement, the resolution statement and the GAGA input of the top level inputs give flat generators of lines, on the whole model and on each component. The existence theorem for [good root towers](/entry/exists-good-root-tower/), with the top level inputs and the Weil pairing statement, then gives a root tower with a good origin satisfying the extra conditions.

For the volume statement, we build the ten inputs of the previous theorem. The top level inputs, the integrability of points, the Weil pairing statement and the comparison statement for pairs are given. The geometric height constants exist by the top level inputs, the Weil pairing statement and the flat degree statement. The Hodge lattice flag bound follows from the existence of local lattice families. The trivial flag statement follows from the Fargues comparison in the top level inputs. The flat degree statement and the twist statement are theorems without hypotheses. The comparison input follows from the inputs of the proof theory, the prime avoidance statement and the resolution statement. The previous theorem applies. $\square$

The constant $C$ depends only on the geometric height constants $C_h$, $C_u$, so it is uniform in the field, the datum, the level and the tower. This uniformity is what Step 4 of the Weil bound needs: the lower bound for the mean slope holds with the same $C$ along every tower, and the term $\Lambda_B$ carries the dependence on the field through its root discriminant and the logarithmic derivative of the $L$-function of the host.

**Remark 9.13.5 (Formalization).** All ten inputs of the first theorem are used. From the top level inputs the proof takes the inputs of the proof theory, the two successive minima bounds, the height bound for Grassmannians and the antisymmetric perturbation statement by position, as the tenth, eleventh, thirteenth and fourteenth parts, and the positivity of agreement is the proved theorem `GlobalTheory.T.agreement_positive` ([VolumeTheoremOfInputs.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/VolumeTheoremOfInputs.lean#L72)). The convergence statement for real towers is applied to the real tower of the origin, but its statement does not use any property of that real tower. The second theorem takes the resolution statement, the Fargues comparison, the GAGA input and the inputs of the proof theory from the top level inputs by position, and the comparison input is built from them; the caller in the chapter on good towers builds the comparison input a second time with the same call ([GoodTowerVolumeTheorem.lean](lean:Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/GoodTowerVolumeTheorem.lean#L36)). The proof of the volume statement does not use the tower of the existence statement: the volume statement is about every good tower. Both second names are statement files whose proofs apply the main theorems. We have not unfolded the geometric height bound, the real tower lemmas or the base settings; the descriptions of items 1 to 11 follow the names and hypotheses of the statements the proof calls.
