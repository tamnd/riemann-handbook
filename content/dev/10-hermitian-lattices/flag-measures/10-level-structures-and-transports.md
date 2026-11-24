---
title: Level structures and transports
decls:
  - GlobalTheory.St.G.LvlZero.level_conj_frame
  - GlobalTheory.T.adelicFrameLevel_conj_formLevel_with_characters
  - GlobalTheory.St.G.level_char_match
  - GlobalTheory.T.exists_adelic_correction_level_character
  - GlobalTheory.St.G.levelConj_holds
  - GlobalTheory.St.SpectralData.exists_transport
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Level structures and transports

This section proves that the level group of a lattice and the level set of an adelic frame are conjugate, with matching characters. It then uses this fact to build a transport from a Hida setting to each given form, with matching lattice, level group and character. The transport is the last part of [the global setting](/entry/exists-setting/) of the next section. The off-diagonal bound of the ninth section uses the global setting through the choice of spectral ties.

### Frames and level groups

Let $E/F$ be a CM extension with complex conjugation $\sigma$, and let $J$ be an invertible hermitian matrix of size $n$ over $E$. Write $U(J)$ for its unitary group and $\mathbb A_f$ for the finite adeles of $F$. Fix a prime $T$, two distinct primes $g_0 \ne g_1$ and an integer $f$ with $[E:\mathbb Q] = 2f$. Assume that $T$, $g_0$ and $g_1$ split in $E$ and that $T \ne g_i$.

A *step level* of type $T$ and level $f$ at the primes over $g_0 g_1$ consists of a lattice $L_b \subset E^n$ of level $T$, an open compact subgroup $U \subset U(J)(\mathbb A_f)$ and a unitary character $\chi$ of $U$. The level group is the stabilizer of the completed lattice $\widehat L_b$ at each place, cut down at the places over $g_0 g_1$.

An *adelic frame* of type $g_0 g_1$ and length $k$ for a lattice $\Lambda$ is a chain of adelic vectors $b_1, \ldots, b_{k}$ and dual vectors $d_1, \ldots, d_k$ adapted to $\Lambda$. Its level set $K(\mathrm{Fr})$ is the set of finite adelic points $y$ that fix the chain modulo the type, and its character is
$$\chi_{\mathrm{Fr}}(y) = \psi\Bigl(g^{-1} \sum_i h(b\, d_i, y\, b_{i+1})\Bigr),$$
where $h$ is the hermitian form of $J$, $g = g_0 g_1$ and $\psi$ is the standard additive character.

**Theorem 3.10.1 (Level conjugation of a frame).** Assume the conditions above, and that the frame length, the size of the step level and the rank all equal $n$. Let $\mathrm{Fr}$ be an adelic frame for $\widehat L_b$. Then there is $\kappa \in U(J)(\mathbb A_f)$ that stabilizes $\widehat L_b$ such that for each $y \in U(J)(\mathbb A_f)$:

1. $y \in K(\mathrm{Fr})$ if and only if $\kappa^{-1} y \kappa \in U$;
2. if $\kappa^{-1} y \kappa \in U$, then $\chi_{\mathrm{Fr}}(y) = \chi(\kappa^{-1} y \kappa)$.

Lean: `GlobalTheory.St.G.LvlZero.level_conj_frame` (also `GlobalTheory.T.adelicFrameLevel_conj_formLevel_with_characters`, a second name).

*Proof.*

1. The lattice $L_b$ has level $T$. By the local description of the dual lattice, $L_b$ is self-dual at each place $v$ that does not divide $T$. So, if $g$ stabilizes the local lattice $L_{b,v}$, then $(g - 1)x \in L_{b,v}$ for each $x$ in the local dual lattice.
2. At each place $v$ over $g_0$ or over $g_1$, the local level match at a type prime gives an element $\kappa_v$ of the local stabilizer of $L_{b,v}$. It conjugates the local level set of the frame onto the local level group and it matches the local characters.
3. Put $\kappa_v = 1$ at all other finite places. Only finitely many places lie over $g_0 g_1$, so $\kappa = (\kappa_v)$ is a finite adelic point. Each $\kappa_v$ stabilizes $L_{b,v}$, so $\kappa$ stabilizes $\widehat L_b$.
4. Compare the two conditions of part 1 place by place. A place cannot lie over both $g_0$ and $g_1$, because $g_0 \ne g_1$. At a place over $g_0$ or over $g_1$, step 2 gives the equivalence. At the other places both conditions say that the local component stabilizes $L_{b,v}$, and step 1 gives the equivalence.
5. Both characters are products of local characters. At places over $g_0 g_1$ the local factors agree by step 2. At the other places both local factors are $1$. This gives part 2. $\square$

**Theorem 3.10.2 (Level correction).** Assume the conditions of the last theorem. Let $\Lambda$ be an adelic lattice and let $h_0 \in U(J)(\mathbb A_f)$ satisfy $h_0^{-1} x \in \widehat L_b$ if and only if $x \in \Lambda$. Let $\mathrm{Fr}$ be an adelic frame for $\Lambda$. Then there is $h_1 \in U(J)(\mathbb A_f)$ such that:

1. $h_1^{-1} x \in \widehat L_b$ if and only if $x \in \Lambda$;
2. $y \in K(\mathrm{Fr})$ if and only if $h_1^{-1} y h_1 \in U$;
3. if $h_1^{-1} y h_1 \in U$, then $\chi_{\mathrm{Fr}}(y) = \chi(h_1^{-1} y h_1)$.

Lean: `GlobalTheory.St.G.level_char_match` (also `GlobalTheory.T.exists_adelic_correction_level_character`, a second name).

*Proof.*

1. Transport the frame along $h_0$. This gives a frame $\mathrm{Fr}'$ for $\widehat L_b$ with $y \in K(\mathrm{Fr})$ if and only if $h_0^{-1} y h_0 \in K(\mathrm{Fr}')$, and with $\chi_{\mathrm{Fr}}(y) = \chi_{\mathrm{Fr}'}(h_0^{-1} y h_0)$.
2. Apply the level conjugation of a frame to $\mathrm{Fr}'$. This gives $\kappa$.
3. Put $h_1 = h_0 \kappa$. Then $h_1^{-1} x = \kappa^{-1}(h_0^{-1} x)$, and $\kappa^{-1}$ stabilizes $\widehat L_b$. This gives part 1.
4. The identity $(h_0\kappa)^{-1} y (h_0 \kappa) = \kappa^{-1}(h_0^{-1} y h_0)\kappa$ and steps 1 and 2 give parts 2 and 3. $\square$

### Level conjugation for forms

Let $D$ be a datum of rank $r$ with a form $F(u)$ for each word $u$. Let $X$ be a Hida setting for $D$. Its level set $K_2$ is a set of finite adelic points with a function $\chi_2$ on it. Say that $X$ *has a level character* if $K_2$ is a subgroup and $\chi_2$ is a unitary character of it.

A *Witt isometry* for $u$ is an isometry $w$ of the hermitian space of $D$ that moves the hyperbolic frame and the vector $z_u$ of $X$ to those of $D$. An *adele isomorphism* $\iota_A$ is an isomorphism of the rings $E \otimes \mathbb A_f$ for $X$ and for $D$ that respects $E$ and the integral adeles. A point $h_0$ *matches the lattice* if $x$ lies in the lattice of $F(u)$ after $h_0^{-1}$ if and only if its image under $w$ and $\iota_A^{-1}$ lies in the column lattice of $X$. A point $h_0$ *matches the level* if, for corresponding points $h$ and $y$, $h$ lies in $K_2$ if and only if $h_0^{-1} y h_0$ lies in the level group of $F(u)$, with equal characters.

**Theorem 3.10.3 (Level conjugation for forms).** Let $X$ have a level character. Let $w$ be a Witt isometry for $u$, let $\iota_A$ be an adele isomorphism, and let $h_0$ match the lattice. Then there is $h_0'$ that matches the lattice and matches the level.

Lean: `GlobalTheory.St.G.levelConj_holds`.

*Proof.*

1. There is an adelic frame $\mathrm{Fr}$ linked to the reference column lattice $M_q(w)$, and $M_q(w)$ is the span part of the transported frame.
2. The record of $D$ gives the facts of the level correction: $T$ and $g_i$ are primes, $T \ne g_i$, all split in $E$, $[E:\mathbb Q] = 2f$, the frame length is the rank, the Gram matrix is hermitian and its determinant is not $0$.
3. Since $h_0$ matches the lattice and $M_q(w)$ is the span part, $h_0^{-1} x \in \widehat L_b$ if and only if $x \in M_q(w)$.
4. The level correction gives $h_1$ with parts 1 to 3 of that theorem. Put $h_0' = h_1$. Part 1 and step 1 give the lattice match.
5. A point lies in the column level set if and only if it lies in the level set of the linked frame, and there the column character equals the frame character. Only this step uses the level character of $X$. With parts 2 and 3 of the level correction, this gives the level match. $\square$

### Transports

A *transport* of $X$ to $F(u)$ consists of a Witt isometry $w$, an adele isomorphism $\iota_A$, a point $h_0$, representatives $h_c$ of $y_c h_0^{-1}$ in the finite group of $X$ for each class $c$ of $F(u)$, and an equivariant conjugate-linear isometry $J$ from the representation space of $X$ at $u$ to functions on frames. A transport *matches the level* if its point $h_0$ matches the lattice and the level.

**Theorem 3.10.4 (Transport).** Let $X$ have a level character, and assume that an adele isomorphism exists. Then for each word $u$ there is a transport of $X$ to $F(u)$ that matches the level.

Lean: `GlobalTheory.St.SpectralData.exists_transport`.

*Proof.*

1. Witt's theorem gives a Witt isometry $w$ for $u$.
2. With the given $\iota_A$, the genus match gives a point $g_0$ that matches the lattice. The reason is that $F(u)$ and the column lattice of $X$ lie in the same genus.
3. The level conjugation for forms replaces $g_0$ by a point $h_0$ that matches the lattice and the level.
4. The representatives $h_c$ exist for each class $c$, and the map $J$ exists. Neither uses the level character. $\square$

The point $g_0$ of step 2 is not kept. Only the corrected point $h_0$ goes into the transport.

**Remark 3.10.5 (Formalization).** The level conjugation of a frame is in AdelicFrameLevelConjFormLevelWithCharacters.lean, line 76, under `set_option maxHeartbeats 2000000`. Its helpers are `not_both_mem`, `finite_mem`, `prVec_sub_one_mulVec` and `mem_hat_of_loc` (lines 27, 41, 55 and 63), in a namespace named `SlopeTestRemainingChoices`. The frame structure `AdFrame`, its level set `InK` and its character `chi` are in SelfDualAt.lean, lines 71, 93 and 98. The step level `StepLevel` is in IsLocBasis.lean, line 58, and the local groups `GLoc` and `GLev` are in PsiZeroNontrivialCharacter.lean, lines 52 and 82. The hypotheses $k = a = s_k = f_c = n$ are four separate equations on natural numbers. The level correction is in ExistsAdelicCorrectionLevelCharacter.lean, line 9. The two statement files (AdelicFrameLevelConjFormLevelWithCharactersStatement.lean and ExistsAdelicCorrectionLevelCharacterStatement.lean, line 8 in each) import the proof modules and close the second names with `first | exact @...`. `LevelConj` is in LevelMatchIff.lean, line 77, and its proof `levelConj_holds` is in LevelConjHolds.lean, line 16. The transport `exists_transport` is in ExistsGlobalSetting.lean, line 32; it calls `wittExists`, `genusMatch_holds`, `levelConj_holds`, `hcExists_all` and `jExists_all`. `Transport` and `LevelMatch` are in ColDict.lean.
