---
title: The symplectic seed in case II
decls:
  - UpperTheory.V.Z.Bc.propMHolZ_alt
  - UpperTheory.Esk.mixSeed_of_alt
  - UpperTheory.V.Z.Bc.seedII_of_p_alt
  - UpperTheory.V.Z.Bc.seedII_Z_alt
  - UpperTheory.V.Z.Bc.seedIIs_alt
  - UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The symplectic seed in case II

This section builds the automorphic seed for case II of the window bound and uses it to prove the symplectic image statement of Section 1. The seed is a four-dimensional [[Galois representation|JQEYEQJY2G]] that is automorphic and has a reduction of a fixed shape. We get it in three steps. First, a congruence between Hilbert modular forms and Eisenstein series gives cuspidal eigenforms whose eigenvalues are residually those of an Eisenstein series. Second, a change of weight turns these eigenforms into ordinary two-dimensional representations with different weights at different places above $l$. Third, induction from a real quadratic field gives a four-dimensional representation, and automorphic induction makes it automorphic. Throughout, $l$ is an odd prime, $\iota\colon \overline{\mathbb{Q}}_l \to \mathbb{C}$ is an isomorphism, $\varepsilon$ is the $l$-adic [[cyclotomic character|XSGB5K2KEG]], and $a \equiv b$ for elements of $\overline{\mathbb{Z}}_l$ means $|a - b| < 1$.

### The Eisenstein congruence

Let $F$ be a totally real field and let $\omega$ be a Hecke character of $F$ of finite order with $\omega_v(-1) = -1$ at each real place $v$. Let $c(w)$ be the conductor exponent of $\omega$ at the finite place $w$. For a place $w$ where $\omega$ is unramified, write $\omega(w)$ for the value of $\omega$ at a uniformizer of $F_w$, viewed in $\overline{\mathbb{Q}}_l$ through $\iota$. Let $P$ be a set of places of $F$. The Eisenstein eigenvalue at $w$ is

$$
e_P(w) =
\begin{cases}
\omega(w) & \text{if } w \mid l \text{ and } w \in P, \\
1 & \text{if } w \mid l \text{ and } w \notin P, \\
1 + \omega(w) & \text{if } w \nmid l \text{ and } c(w) = 0, \\
1 & \text{otherwise.}
\end{cases}
$$

**Theorem 8.7.1 (Eisenstein congruence for Hilbert forms).** Assume the extended hypotheses, the existence of [Hecke's weight one Eisenstein series](/entry/hilbert-eisenstein-weight-one-holds/) and the existence of [forms congruent to one in a large weight](/entry/one-use/). Let $F$, $\omega$, $c$ and $P$ be as above. Assume that $c(w) \neq 0$ for some $w$, that $c(w) = 0$ for each $w \mid l$, that there is $w \in P$ above $l$ with $\omega(w) \not\equiv 1$, and that there is $w' \notin P$ above $l$ with $\omega(w') \not\equiv 1$. Then for each $B$ there are an integer $k \geq B$ with $l - 1 \mid k$ and a cuspidal holomorphic Hilbert eigenform $g$ of parallel weight $k + 1$, character $\omega$ and level $\Gamma_1(w)$ at $w \mid l$ and conductor $c$ elsewhere, whose eigenvalues satisfy $\lambda_w(g) \equiv e_P(w)$ for every finite place $w$.

Lean: `UpperTheory.V.Z.Bc.propMHolZ_alt`.

*Proof.* Hecke's weight one Eisenstein series $E(1, \omega)$, stabilized at each $w \mid l$ with the root $\omega(w)$ if $w \in P$ and the root $1$ if $w \notin P$, gives a Hilbert form $E$ of weight one with integral coefficients, with first coefficient $a(1) = 1$, whose eigenvalues are $e_P(w)$. By the second input there is a form $h$ of parallel weight $k \geq B$ with $l - 1 \mid k$, integral coefficients and $h \equiv 1$. The product $Eh$ has weight $k + 1$, integral coefficients, and the same reduction as $E$. So the reduction of $Eh$ is an eigenform modulo the maximal ideal with eigenvalues $e_P(w)$. The lifting lemma of Deligne and Serre, which is part of the extended hypotheses, gives an eigenform $g$ of weight $k + 1$ and the same level with $\lambda_w(g) \equiv e_P(w)$ for all $w$.

It remains to show that $g$ is cuspidal. Assume that it is not. Then $g$ is an Eisenstein series $E(\eta_1, \eta_2)$ for two Hecke characters of finite order with $\eta_1 \eta_2 = \omega$. At a place $w \nmid l$ with $c(w) = 0$ its eigenvalue is $\eta_1(w) + \eta_2(w) \mathrm{N}w^k$. As $\mathrm{N}w$ is prime to $l$ and $l - 1 \mid k$, we have $\mathrm{N}w^k \equiv 1$. So

$$
\eta_1(w) + \eta_2(w) \equiv 1 + \eta_1(w)\eta_2(w),
$$

that is, $(\eta_1(w) - 1)(\eta_2(w) - 1) \equiv 0$. By global Artin reciprocity, the reductions of $\eta_1$ and $\eta_2$ are characters of a Galois group, and the Frobenius elements at these places are dense. A group is not the union of two proper subgroups, so for every idele $x$ we have $\eta_1(x) \equiv 1$ or $\eta_2(x) \equiv 1$. At the places above $l$, the eigenvalues give $\eta_1(w) \equiv \omega(w)$ for $w \in P$ and $\eta_1(w') \equiv 1$ for $w' \notin P$. Take $w$ and $w'$ as in the hypotheses and let $x = \varpi_w \varpi_{w'}$ be the product of the two uniformizers. Then $\eta_1(x) \equiv \omega(w)$ and $\eta_2(x) = \omega(x)\eta_1(x)^{-1} \equiv \omega(w')$. Either case gives $\omega(w) \equiv 1$ or $\omega(w') \equiv 1$, which is false. So $g$ is cuspidal. $\square$

### Ordinary lifts with mixed weights

A Galois representation $r\colon G_F \to \mathrm{GL}_2(\overline{\mathbb{Q}}_l)$ is ordinary at $w \mid l$ with weights $(a, b)$ if its restriction to the decomposition group at $w$ is upper triangular, with a character of Hodge-Tate weight $a$ on the line and a character of Hodge-Tate weight $b$ on the quotient.

**Theorem 8.7.2 (Ordinary lifts with mixed weights).** Assume the extended hypotheses and the Eisenstein congruence for Hilbert forms. Let $F$ be a totally real field of even degree in which $l$ splits completely. Let $\xi$ be a character of $G_F$ with open kernel that is odd at each complex conjugation, unramified above $l$ and ramified at some place of norm $2$. Assume that $\xi^2$ is not residually trivial and that $\xi$ is not residually trivial on the decomposition group of each place above $l$. Let $P$ be a set that holds some, but not all, of the places above $l$. Then there are integers $k, t \geq 2$ with $l - 1 \mid k$ and $l - 1 \mid t$, a cuspidal automorphic representation $\pi$ of $\mathrm{GL}_2$ over $F$, and a continuous representation $r$ of $G_F$ attached to $\pi$ and irreducible on each open subgroup, such that:

1. $\det r = \varepsilon^k \xi$, and the reduction of $r$ has semisimplification $1 \oplus \bar\xi$;
2. at each $w \in P$ above $l$, $r$ is ordinary with weights $(k + t, -t)$;
3. at each $w \notin P$ above $l$, $r$ is ordinary with weights $(k, 0)$;
4. $\pi$ has the infinitesimal characters that match these weights, and $r$ meets the local conditions of a lift away from $l$.

Lean: `UpperTheory.Esk.mixSeed_of_alt`.

*Proof.* We give the steps. By class field theory, $\xi$ is a Hecke character $\omega$ of finite order. It is odd at each real place, unramified above $l$ and ramified at a place of norm $2$, so the conductor is not trivial. Since $\xi$ is not residually trivial at any place above $l$, the hypotheses of the Eisenstein congruence hold for $\omega$ and $P$. This gives an eigenform $g$ of parallel weight $k + 1$, with $k$ as large as we want and $l - 1 \mid k$, whose eigenvalues are congruent to $e_P(w)$. The weight-changing congruence of Hilbert forms raises the weight of $g$ by $2t$, with $l - 1 \mid t$, at a chosen set of infinite places and keeps the congruence. As $l$ splits completely, the places above $l$ match the infinite places through $\iota$. Choose the infinite places that match $P$. The result is a cuspidal eigenform of mixed weight whose Galois representation $r$ has determinant $\varepsilon^k \xi$. Its Frobenius traces are congruent to $1 + \xi(w)$, so by the Chebotarev density theorem and the theorem of Brauer and Nesbitt the reduction is $1 \oplus \bar\xi$. The eigenvalue $\xi(w)$ or $1$ at $w \mid l$ is a unit, so $r$ is ordinary at $w$, and the weights are $(k + t, -t)$ at $w \in P$ and $(k, 0)$ at $w \notin P$. The representation is not induced, since $\xi^2$ is not residually trivial, and so it is irreducible on each open subgroup. $\square$

### The seed of case II

Let $D$ be good raw data in case II with a tower $T$ that is complete, of depth two and deep, as in Section 1. The tower holds a totally real field $F_T$, a totally complex field $L$ that contains it, and an open subgroup $G'$ of $G_{F_T}$. A seed for $D$ and $T$ is a larger coefficient datum $c_1 \supseteq c$ and a seed pair $Q$ with three properties:

1. the $l$-adic representation of $Q$ is irreducible and, after a twist, it is attached to a regular algebraic cuspidal representation of $\mathrm{GL}_4$ over $L$, with weights $2m_0 + b > 2m_1 + b > 2m_2 + b > 2m_3 + b$ where $m_i - m_{i+1} \geq 2$;
2. the reduction of $Q$ meets the Frobenius condition of the tower;
3. the reduction has a nonzero entry of root weight $(-1, 0)$, or nonzero entries of root weights $(-1, 1)$ and $(-1, -1)$.

We use two forms of the inputs over a tower. The tower form of mixed lifts says: for the real quadratic field $k_0$ and the quadratic character $\varphi$ of $G_{\mathbb{Q}}$ that a tower defines, the conclusion of the previous theorem holds over $k_0$, with the character $\xi$ of $D$. The induced automorphy statement says: for induction data $(k_0, \varphi, k, t, r, \alpha, \beta, R, \delta)$ over $T$, where $r$ is a lift over $k_0$ and $R$ is a four-dimensional representation of $G_{\mathbb{Q}}$ built from $r$ by induction, the twist of $R$ by $\delta$ is automorphic over $L$ and meets the weight condition.

**Theorem 8.7.3 (Seed of case II from mixed lifts).** Assume the tower form of mixed lifts and the induced automorphy statement. Then each good datum in case II with a complete, deep tower of depth two has a seed.

Lean: `UpperTheory.V.Z.Bc.seedII_of_p_alt`.

*Proof.* Fix $D$, $T$ and $\iota$.

Step 1. The tower gives a subgroup of index two of $G_{\mathbb{Q}}$ that contains the image of $G_{F_T}$. Its fixed field is a real quadratic field $k_0$, and $\varphi$ is the quadratic character with kernel $G_{k_0}$. The residual characters of $D$ split over $k_0$ in the way that the mixed lifts need.

Step 2. The tower form of mixed lifts gives $k$, $t$ and a lift $r_0$ over $k_0$. Since the square of the image of the generator $g_0$ of the tower lies in $G_{k_0}$, Ribet's lattice argument gives a conjugate $r$ of $r_0$ whose reduction is a nonsplit extension in the required direction. All properties of $r_0$ pass to $r$. Put $\mu = \varepsilon^k \xi \varphi$. As $\varphi$ is trivial on $G_{k_0}$, we get $\det r = \mu|_{G_{k_0}}$.

Step 3. Induction from $k_0$ to $\mathbb{Q}$ and a twist give the induction data $(k_0, \varphi, k, t, r, \alpha, \beta, R, \delta)$, where $\alpha$ and $\beta$ are units and $\delta$ is a character of $G_{F_T}$. The restriction of $R$ to $G'$ is irreducible, because $r$ is irreducible on open subgroups and its two conjugates under $\mathrm{Gal}(k_0/\mathbb{Q})$ have different weights at the places above $l$.

Step 4. The local analysis at the places above $l$ gives integers $n$, $m_0, \ldots, m_3$, $b$ and $N$, with $m_i - m_{i+1} \geq 2$, such that the twist of $R$ by $\delta$ has Hodge-Tate weights $2m_i + b$, and $\delta^{-1}$ and $\varepsilon$ satisfy the relation that the final statement needs.

Step 5. The induced automorphy statement gives a regular algebraic cuspidal $\pi$ over $L$ that is attached to the restriction of $R \otimes \delta$ to $G_L$. Let $Q$ be the pair made of $R \otimes \delta$ and $n$. A constituent of the induced representation vanishes, and this gives the global part of the reduction conditions 2 and 3. Condition 1 holds with the weights of Step 4 and with $\pi$. $\square$

**Theorem 8.7.4 (Seed of case II).** Assume the extended hypotheses. Then each good datum in case II with a complete, deep tower of depth two has a seed.

Lean: `UpperTheory.V.Z.Bc.seedIIs_alt` (also `UpperTheory.V.Z.Bc.seedII_Z_alt`, the form with the three inputs and induced automorphy as hypotheses).

*Proof.* The Eisenstein congruence needs the extended hypotheses, Hecke's weight one Eisenstein series and the forms congruent to one. The last two are published results, and the first is the hypothesis. So the Eisenstein congruence for Hilbert forms holds. With the extended hypotheses, the theorem on ordinary lifts with mixed weights holds, and its tower form follows by restriction to the field $k_0$ of a tower.

The induced automorphy statement follows from the extended hypotheses with three inputs. The first is the lift of quadratic base change from real to complex fields, which comes from the base change part of the extended hypotheses. The second is the lift of cyclic base change in rank two, which comes from the cyclic part. The third is [automorphic induction from $\mathrm{GL}_2$ to $\mathrm{GL}_4$](/entry/ind-cs/) of Section 8. The previous theorem now gives the seed. $\square$

### The symplectic image statement

**Theorem 8.7.5 (Symplectic image statement).** Assume the extended hypotheses. Let $h$ be a host datum that is large for $t$, let $0 < e < t$, let $\psi$ be a character for $h$, $c$ and $e$, and let $D$ be good raw data in case II or case III of $(h, e, \psi)$. Then $D$ is finite and has no end, and there is $\iota$ such that each irreducible piece of $D$ is automorphic of dimension four.

Lean: `UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt`.

*Proof.* By the [promodularity and automorphy theorem in rank four](/entry/sp4-in-alt/), the statement follows from five inputs:

1. the inputs from [[Galois cohomology|9MPCZ3EAJM]], that is, Poitou-Tate duality, the global Euler characteristic formula and the formula of Greenberg and Wiles;
2. the theorem of Ferrero and Washington (Ann. of Math. 109, 1979): for an abelian field $K$ that contains $\mu_l$, the $l$-rank of the class group is bounded along the cyclotomic $\mathbb{Z}_l$-extension of $K$, so the $\mu$-invariant of [[Iwasawa theory|Y2SPPSQ5D4]] vanishes;
3. the seed of case II;
4. [the seed of case III](/entry/fourth-initial-of-prints-h/);
5. [the potential modularity towers](/entry/pm-ex-of-prints-h/).

The extended hypotheses give the first input through the adjoint lifting theorem, which carries the cohomology inputs. The second is a published theorem. The previous theorem gives the third. The fourth and fifth follow from the extended hypotheses. $\square$

**Remark 8.7.6 (Formalization).** Every file in this section sets `maxHeartbeats 800000`, also where the proof is one line: [MixSeedOf.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MixSeedOf.lean#L8) and [SeedIIZ.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/SeedIIZ.lean#L10). The ordinary lifts with mixed weights are one application of a general lemma to the weight-changing congruence `holWC`, and `holWC` is proved in a second file with the same name, [MixSeedOf.lean](lean:PositivityTheory/AutomorphicForms/PublishedInputs/JacquetLanglands/TorusKernels/MixSeedOf.lean#L8), in another tree. The Eisenstein congruence is in [MPropMHol.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/MPropMHol.lean#L108), and the step with global Artin reciprocity is the private lemma `gal_of` at line 83. The seed of case II is proved in [BcIndCs.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/BcIndCs.lean#L16), whose name refers to the input `indCs` and not to the theorem. The seed, the tower conditions and the lift conditions are the predicates `SeedIIAlt`, `Ctx2`, `Ok`, `Two`, `Deep`, `PR` and `TypeAway`; we state them in words and do not unfold them. In the symplectic image statement, `SymplecticFourImageDense` puts $\iota$ under an existential quantifier ([IsAut4.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/IsAut4.lean#L14)).
