---
title: Doubled models, toric sums and square flips
decls:
  - GlobalTheory.T.exists_doubledWeil_blockEmbedding_acts_on_first_boxFactor
  - GlobalTheory.DblSchr.doubledModel
  - GlobalTheory.ToricSumValue.toricSum_eq
  - GlobalTheory.T.squareFlip_reaches_localQuotient_classes
  - GlobalTheory.SquareFlipReach.flip_reach
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Doubled models, toric sums and square flips

Three more inputs of [the nonempty hypotheses of the definite side](/step/nonempty-hyps/) are proved here. The first is the doubling construction for the Weil representation: a Schrödinger model for the doubled hermitian space in which the diagonal Lagrangian satisfies the Siegel rule and the first factor of a box product carries the original representation. The second evaluates a sum of lattice sums over the ring class group as a Hecke $L$-value times explicit local factors. The third shows that every local quotient class of the Weil representation is reached by a block translate of the local function of a square flip.

### The doubled Schrödinger model

Let $F$ be the totally real field of the host and $E$ its CM extension, with adeles $\mathbb{A}_F$ and $\mathbb{A}_E$. Let $\psi$ be a standard additive character of $\mathbb{A}_F$ of sign $-1$. Let $S$ and $T$ be hermitian spaces with Gram matrices $G_S$ and $G_T$, and $\chi_S, \chi_T$ Hecke characters of $E$ whose restrictions to $\mathbb{A}_F^\times$ are $\eta^{\dim S}$ and $\eta^{\dim T}$, with $\eta$ the quadratic character of $E/F$. Put
$$\begin{aligned} J_A &= G_T^{\mathsf{T}}, & \xi\, J_B &= \xi_0\, G_S^{-1}, \end{aligned}$$
for an element $\xi$ of $\mathbb{A}_F \otimes_F E$. The space $\mathbb{W}$ of $\dim T \times \dim S$ matrices over $\mathbb{A}_E$ is symplectic for the form built from $\xi$, $J_A$ and $J_B$, and the unitary groups $U(J_A)$ and $U(J_B)$ act on it.

Let $(y, z)$ be Darboux coordinates of $\mathbb{W}$ indexed by a finite set $\kappa$, rational in the sense that rational matrices have rational coordinates, and let $\omega_0$ be the Schrödinger representation of $U(J_A) \times U(J_B)$ on functions of $y \in \mathbb{A}_F^\kappa$, obtained by transport from a Weil datum $\omega$ of the pair $(S, T)$. Put
$$\begin{aligned} J_B^{\Box} &= \begin{pmatrix} J_B & 0 \\ 0 & -J_B \end{pmatrix}, & C_\Delta &= \begin{pmatrix} 1 \\ 1 \end{pmatrix}, \end{aligned}$$
so that the columns of $C_\Delta$ span the diagonal of the doubled space. For functions $\varphi_1, \varphi_2$ of $y \in \mathbb{A}_F^\kappa$, the *box product* is $(\varphi_1 \boxtimes \varphi_2)(y_1, y_2) = \varphi_1(y_1)\, \varphi_2(y_2)$ on $\mathbb{A}_F^{\kappa \sqcup \kappa}$.

**Theorem 7.37.1 (The doubled Schrödinger model).** In this situation there are Darboux coordinates $d^{\Box}$ for the symplectic space of $J_A$ and $J_B^{\Box}$, indexed by $\kappa \sqcup \kappa$, and a representation $\omega^{\Box}$ of $U(J_B^{\Box})$ on functions of $\mathbb{A}_F^{\kappa \sqcup \kappa}$, such that:

1. $d^{\Box}$ is the doubled coordinate system: it maps $(w_1 \mid w_2)$ to $(y_1 \sqcup y_2,\ z_1 \sqcup (-z_2))$, where $(y_i, z_i)$ are the coordinates of $w_i$;
2. $C_\Delta$ spans a Lagrangian for $J_B^{\Box}$, and $\omega^{\Box}$ is a unitary splitting of the metaplectic cover attached to $\chi_T$;
3. the Siegel rule holds: for every admissible functional $l$ that is invariant under the translations by $C_\Delta$, every $p \in U(J_B^{\Box})$ with $p\, C_\Delta = C_\Delta\, t$ for some $t \in \mathrm{GL}$, and every Schwartz-Bruhat function $\varphi$,
$$\begin{aligned} l(\omega^{\Box}(p)\varphi) &= \chi_T(\det t)\, |\mathrm{N}(\det t)|^{\dim T / 2}\, l(\varphi); \end{aligned}$$
4. for $g \in U(J_B)$ and $g^{\Box} \in U(J_B^{\Box})$ with matrix $\operatorname{diag}(g, 1)$, and Schwartz-Bruhat functions $\varphi_1, \varphi_2$,
$$\begin{aligned} \omega^{\Box}(g^{\Box})(\varphi_1 \boxtimes \varphi_2) &= \omega_0(1, g)\varphi_1 \boxtimes \varphi_2. \end{aligned}$$

Lean: `GlobalTheory.T.exists_doubledWeil_blockEmbedding_acts_on_first_boxFactor` (also `GlobalTheory.DblSchr.doubledModel`).

*Proof.* The doubled hermitian space $S \oplus (-S)$ with the pair of characters $(\chi_S, \chi_T)$ has a Weil datum $\omega^{\Box}_0$, and its Schrödinger transport to the coordinates $d^{\Box}$ gives $\omega^{\Box}$. Property 1 holds by the construction of $d^{\Box}$ from the coordinates of the two copies. For property 2, the diagonal is isotropic for $J_B^{\Box}$, since $C_\Delta^{\mathsf{T}} J_B^{\Box} \bar C_\Delta = J_B - J_B = 0$, and the antidiagonal is a complement of the same kind; the transported Weil datum is a unitary splitting because the original one is. Property 3 is the Siegel rule of the doubled model. Property 4 holds because the transport of the Weil datum of $S \oplus (-S)$ restricts on $U(S) \times U(-S)$ to the tensor product of the two Weil data, and on the first factor this is $\omega_0$. $\square$

The Siegel rule is the classical reason why doubling works. In a model attached to a Lagrangian, the stabilizer $P$ of that Lagrangian acts on the value at the origin by a character: the unipotent radical acts by translations, which $l$ ignores, and an element $p$ with Levi part $t$ acts by $\chi(\det t)$ times the modulus $|\mathrm{N}(\det t)|^{\dim T/2}$. So $l(\omega^{\Box}(g)\varphi)$ is a section of the degenerate principal series of $U(J_B^{\Box})$ induced from the Siegel parabolic, which is the starting point of the doubling method of Piatetski-Shapiro and Rallis. This paragraph gives the classical argument; the Lean proof cites `siegelRule_diagonal_doubledSchroedingerModel` for it.

### The toric sum

Let $E$ be a CM field with maximal real subfield $E^+$, $\Phi = (\varphi_i)_{i \in I}$ a CM type of $E$, $s \geq 1$ an integer and $\kappa \colon I \to \mathbb{N}$. Let $\mathfrak{f}$ be an ideal of $\mathcal{O}_{E^+}$ satisfying the base conditions: it is nonzero and proper, and each prime divisor $v$ of $\mathfrak{f}$ splits in $E$, divides $\mathfrak{f}$ at most twice, and lies over an odd prime $\ell$ that is prime to the discriminant of $E$ and has residue degree one in $E$. Let $Q$ be a finite set of primes of $E^+$ that split in $E$ and do not divide $\mathfrak{f}$, and put $\mathfrak{c} = \mathfrak{f} \prod_{q \in Q} q$.

For $x \in E^\times$ and $\sigma \in \mathbb{C}$ put
$$\begin{aligned} \mathrm{term}(x, \sigma) &= \prod_{i \in I} \varphi_i(x)^{-(2s + \kappa_i)}\, \overline{\varphi_i(x)}^{\,\kappa_i}\, |\varphi_i(x)|^{-2\sigma}. \end{aligned}$$
For a lattice $L$ in $E$, the *lattice sum* of $L$ is an entire function $S_L$ with $S_L(\sigma) = \sum_x \mathrm{term}(x, \sigma)$ for $\operatorname{Re}\sigma > 1 - s$, the sum over the nonzero $x \in L$ modulo units. Let $\mathrm{Pic}(\mathfrak{c})$ be the ring class group of the order of conductor $\mathfrak{c}$, and for each class $q$ let $L_q$ be the lattice of a fixed representative $\hat q$. A number $T$ is the *toric sum* of $\chi$ for $\mathfrak{c}$ if $\mathrm{Pic}(\mathfrak{c})$ is finite, each $L_q$ has a lattice sum $S_q$, and
$$\begin{aligned} T &= \sum_{q \in \mathrm{Pic}(\mathfrak{c})} \bigl(\chi_f(\hat q)\, \lVert \hat q \rVert^{s}\bigr)^{-1} S_q(0), \end{aligned}$$
where $\chi_f$ is the finite part of $\chi$ and $\lVert \cdot \rVert$ the idelic norm. For $N$, $s$ and $a$ put
$$\begin{aligned} \mathrm{eq}(N, s, a) &= (1 - a N^{-s})(1 - a^{-1} N^{-s}) + (N - 1) N^{-2s}. \end{aligned}$$

**Theorem 7.37.2 (Toric sums are Hecke values).** Assume that the $L$-function of every unitary Hecke character of a CM field with nonzero infinity type continues to an entire function. Let $E$, $\Phi$, $s$, $\kappa$, $\mathfrak{f}$ and $Q$ be as above, with $E/E^+$ unramified at all finite places. Let $\chi$ be a unitary Hecke character of $E$, trivial on the ideles of $E^+$, of infinity type $(\kappa_i + s)_i$, of level at most $1$ at the primes over $Q$, and of exponent $\operatorname{ord}_v \mathfrak{f}$ at the primes over $v \notin Q$. For each $q \in Q$ let $P_q$ be a prime of $E$ over $q$, and let $\Lambda$ be the entire function with $\Lambda(z) = \prod_P L_P(\chi, z)$ for $\operatorname{Re} z > 1$. Then
$$\begin{aligned} \Lambda(s) \prod_{\substack{q \in Q \\ \chi \text{ unramified at } P_q}} \mathrm{eq}\bigl(\mathrm{N}q,\ s,\ \chi(P_q)\bigr) \end{aligned}$$
is the toric sum of $\chi$ for $\mathfrak{c}$.

Lean: `GlobalTheory.ToricSumValue.toricSum_eq`.

*Proof.* We follow the Lean proof.

1. The conductor $\mathfrak{c}$ is nonzero, so the ring class group $\mathrm{Pic}(\mathfrak{c})$ is finite.
2. The finite part of $\chi$ is trivial on the units of the order, by the conditions on the exponents of $\chi$.
3. For each class $q$, the lattice sum of $L_q$ exists. Its Dirichlet series converges for $\operatorname{Re}\sigma > 1 - s$, and its continuation to an entire function comes from the assumption on Hecke $L$-functions, applied to the twists of $\chi$ by the characters of $\mathrm{Pic}(\mathfrak{c})$.
4. Consider the two entire functions of $\sigma$:
$$\begin{aligned} A(\sigma) &= \sum_{q} \bigl(\chi_f(\hat q)\, \lVert \hat q \rVert^{s + \sigma}\bigr)^{-1} S_q(\sigma), & B(\sigma) &= \Lambda(s + \sigma) \prod_{q} \mathrm{eq}\bigl(\mathrm{N}q,\ s + \sigma,\ \chi(P_q)\bigr). \end{aligned}$$
For $\operatorname{Re}\sigma > 1 - s$, both are the sum of $\chi_f(y)^{-1}\lVert y \rVert^{-(s + \sigma)}$ over the integral ideles $y$ of the order modulo units. For $A$, this is the decomposition of that sum by classes: an integral idele in the class $q$ is $k\, \hat q^{-1}$ times a unit, with $k \in E^\times$, and its term is the term of $k$. For $B$, it is the Euler product of the same sum, whose factors are $L_P(\chi, s + \sigma)$ at the primes away from $Q$ and the factors $L_P \cdot \mathrm{eq}$ of the order at the primes over $Q$.
5. Two entire functions that agree on a half plane are equal, so $A = B$, and at $\sigma = 0$ this is the theorem.

This proves the theorem. $\square$

The local factor in step 4 is the local zeta function of the order $\mathcal{O}_{E^+, q} + q\, \mathcal{O}_{E, q}$ at a split prime $q$: the ideles of the order are the pairs $(a, b) \in F_q^\times \times F_q^\times$ with $a \equiv b \bmod q$ up to units, and the sum of their terms is $L_{P_q} L_{\bar P_q} \cdot \mathrm{eq}$. We have not opened the Lean proof of the Euler product, `hasSum_integralIdeles_eulerProduct`, and this description is the classical computation.

### Square flips reach the local quotient classes

Let $G$ be a grid with a Weil datum and frames, $t$ an index in square standing, $i, j$ steps, $M$ a volume and $e$ a numerator, and let $(\psi, \Gamma, X, \omega, \omega')$ be a triple of $t$, matched with real and finite maps and tied to $t$. The finite maps give, at each finite place $v$ of $F$, a local space $\Pi_v$ and two linear maps
$$\begin{aligned} p_v &\colon \mathcal{S}(\mathrm{Mat}_{a \times (a + a')}(F_v)) \to \Pi_v, & p'_v &\colon \mathcal{S}(\mathrm{Mat}_{a' \times (a + a')}(F_v)) \to \Pi_v, \end{aligned}$$
from the Schwartz-Bruhat spaces of the big and the small model. The classes $p_v(\varphi)$ are the *local quotient classes*. At a local place $w$ of $t$, a *natural datum* of level $n$ for the uniformizer at $w$ gives the *square flip* of level $n$, a function in the model of the grid, and a *local function* of the flip is a Schwartz-Bruhat function of the big model at $v$ that represents it.

**Theorem 7.37.3 (Square flips reach the local quotient classes).** Let $w$ be a local place of $t$ over the place $v$ of $F$, and $\varphi_0$ a Schwartz-Bruhat function of the big model at $v$. Then there are $n \geq \operatorname{depth}(w)$, a natural datum $\Phi$ of level $n$, a local function $\varphi_2$ of the square flip of $\Phi$, an element $g$, and a Schwartz-Bruhat function $\varphi_3$ with
$$\begin{aligned} \varphi_3 &= \omega(1, u_e(g))\, \varphi_2, & p_v(\varphi_3) &= p_v(\varphi_0), \end{aligned}$$
where $u_e(g)$ is the block embedding of $g$ given by $e$.

Lean: `GlobalTheory.T.squareFlip_reaches_localQuotient_classes` (also `GlobalTheory.SquareFlipReach.flip_reach`).

*Proof.* Since the triple is tied to $t$, the place $v$ lies in the set of places of the characters, and so in the set of places of the base.

1. The matching gives two zeta integral maps $\iota_A$ and $\iota_B$ at $v$ for the big and the small model, with the following property: for $\varphi$ in the big model and $\varphi'$ in the small model, $p_v(\varphi) = p'_v(\varphi')$ if and only if the big zeta integral of $\iota_A \varphi$ equals the small zeta integral of $\iota_B \varphi'$.
2. The map $p'_v$ is onto the image of $p_v$, so there is $\varphi'$ with $p'_v(\varphi') = p_v(\varphi_0)$, and $\Psi = \iota_B \varphi'$ is a Schwartz-Bruhat function.
3. The realization of the triple in the square class gives a Lagrangian model $\iota$, a constant $c \neq 0$ and matrices $g_0$ and $c_0$ such that for every $n \geq \operatorname{depth}(w)$ and every natural datum $\Phi$ of level $n$ there is $\varphi_2$ with $\iota \varphi_2$ the square flip of $\Phi$ and
$$\begin{aligned} \iota_A \varphi_2(Z) &= c \cdot \mathrm{sq}_\Phi\bigl(g_0\, Z\, c_0\bigr), \end{aligned}$$
where $\mathrm{sq}_\Phi$ is the core of the flip read through the transport at $v$. The same realization shows that for all blocks $K_1, K_2$ there are $g$ and $c' \neq 0$ such that $\omega(1, u_e(g))$ acts on $\iota_A$ by $\iota_A \varphi_3(Z) = c' \cdot \iota_A \varphi(Z c_0 \operatorname{blk}(K_1, K_2) c_0^{-1})$.
4. The zeta integral of the block translates of the flip core takes every value: for the scalars $c\, c'(K_1, K_2) \neq 0$ of step 3, there are $n$, $\Phi$, $K_1$ and $K_2$ such that the big zeta integral of $Z \mapsto c\, c'\, \mathrm{sq}_\Phi(g_0 Z c_0 \operatorname{blk}(K_1, K_2))$ equals the small zeta integral of $\Psi$.
5. Take $\varphi_2$ for these $n$ and $\Phi$, and $\varphi_3$ for these $K_1, K_2$. Then $\iota_A \varphi_3$ is the function of step 4, so its big zeta integral is the small zeta integral of $\iota_B \varphi'$, and step 1 gives $p_v(\varphi_3) = p'_v(\varphi') = p_v(\varphi_0)$.

This proves the theorem. $\square$

**Remark 7.37.4 (Formalization).** The relay `exists_doubledWeil_blockEmbedding_acts_on_first_boxFactor` is at line 15 of [DoubledSchroedingerModelSiegelRuleStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DoubledSchroedingerModelSiegelRuleStatement.lean#L15), under `maxHeartbeats 1000000`, and its target `doubledModel` is at line 20 of [DoubledSchroedingerModelSiegelRule.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/DoubledSchroedingerModelSiegelRule.lean#L20). Its proof is a single `refine` of cited lemmas: `exists_doubledPairWeilDatum_schrodingerTransport`, `isDblCoord_dblD`, `isLagr_diagCols`, `isUnitarySplitting_transportedDoubledWeilDatum` and `siegelRule_diagonal_doubledSchroedingerModel`. Property 4 is proved at line 52 by the lemma `realGram_hermitianSpaceDoubled_blockDiagonal`, whose name does not describe the box factor statement; it is the only place where the Weil datum $\omega$ and the transport hypothesis are used. The definitions `dbl`, `diagCols`, `boxFun`, `IsDblCoord`, `SiegelRule` and `IsUWeilSplit` are in [HilbertNinetyQuotientHomEqIff.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/HilbertNinetyQuotientHomEqIff.lean#L337). The theorem `toricSum_eq` is at line 95 of [ToricSumEqHeckeLValueMulAuxiliaryFactors.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ToricSumEqHeckeLValueMulAuxiliaryFactors.lean#L95), with `hasSum_classes` at line 72 for the class decomposition of step 4. The relay `toric_sum_eq_hecke_L_value_mul_auxiliary_factors` at line 7 of the companion statement file is not in the outline. The continuation hypothesis is an argument of the theorem; its users supply it as `exists_isHeckeL_of_hasInf` or `HeckeEntire_holds`. The definition `IsToricSum` is at line 101 of [EntireEqOfHalfPlane.lean](lean:Development/AbelianVarietyTheory/Definitions/Divisors/EntireEqOfHalfPlane.lean#L101). The relay `squareFlip_reaches_localQuotient_classes` is at line 17 of [SquareFlipReachesLocalQuotientClassesStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SquareFlipReachesLocalQuotientClassesStatement.lean#L17), under `maxHeartbeats 1000000`. The target `flip_reach` is at line 73 of [SquareFlipReachesLocalQuotientClasses.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/SquareFlipReachesLocalQuotientClasses.lean#L73). It applies `flip_reach_of` (line 18), which takes steps 3 and 4 as explicit hypotheses `G1` and `G2`, to the cited statements `theta_triple_realization_square_class` and `zetaIntegral_block_translate_of_flip_datum`. Both theorems are declared with their full names `GlobalTheory.SquareFlipReach.*` outside any namespace. The reasons given for properties 2 and 4 of the doubled model, and in step 3 of the proof for the toric sum, are classical arguments; the Lean proofs cite the lemmas named here and `exists_entire_latticeSum_of_heckeL_continuation`. The proofs of the cited lemmas were not opened.
