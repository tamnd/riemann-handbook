---
title: Segment representations of GL(n) over a p-adic field
decls:
  - CompanionTheory.RgGu.NR.redClC
  - CompanionTheory.RgGu.NR.rhoNuRhoReducibleC
  - CompanionTheory.RgGu.segmentRepresentation
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Segment representations of GL(n) over a p-adic field

Let $\sigma$ be an irreducible cuspidal representation of $\mathrm{GL}_d$ over a $p$-adic field. The induced representation $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$ has a unique irreducible subrepresentation, and its Jacquet module is the single tensor product $\sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$. These are Zelevinsky's segment representations, the building blocks of the classification of irreducible representations of $\mathrm{GL}_n$. This section proves the existence, uniqueness and Jacquet module of the segment representation, starting from the reducibility of $\sigma \times \sigma\nu$. The result is used in the step [EveryCharacter](/step/every-character/).

Background: [parabolic induction and the Jacquet module](/learn/representations/#parabolic-induction-and-the-jacquet-module), [cuspidal representations and segments](/learn/representations/#cuspidal-representations-and-segments), [[cuspidal representation|9AZ164C298]].

### Notation

Let $k$ be a nonarchimedean local field and $\nu = |\det|$ the absolute value of the determinant, on $\mathrm{GL}_d(k)$ for each $d$. All representations are complex representations, without topology on the space. A representation is *smooth* if every vector has an open stabiliser.

For $d_1, \dots, d_h$ with sum $N$ and representations $\pi_a$ of $\mathrm{GL}_{d_a}(k)$, let $\pi_1 \times \dots \times \pi_h$ be the normalised parabolic induction of $\pi_1 \otimes \dots \otimes \pi_h$ from the standard block upper triangular parabolic subgroup $P$ with Levi factor $M = \prod_a \mathrm{GL}_{d_a}(k)$: the smooth functions $f$ on $\mathrm{GL}_N(k)$ with $f(p g) = \delta_P^{1/2}(p)\, (\pi_1 \otimes \dots \otimes \pi_h)(p) f(g)$. For a representation $\pi$ of $\mathrm{GL}_N(k)$, let $r_M(\pi)$ be its normalised Jacquet module: the coinvariants of the unipotent radical of $P$, with the action of $M$ twisted by $\delta_P^{-1/2}$.

**Definition 2.7.1 (Cuspidal).** A smooth representation $\pi$ of $\mathrm{GL}_d(k)$ is *cuspidal* if $r_M(\pi) = 0$ for every proper standard Levi subgroup $M$.

For an irreducible cuspidal $\sigma$ of $\mathrm{GL}_d(k)$ and $l \geq 1$, the *segment* $[\sigma, \sigma\nu^{l-1}]$ is the sequence $\sigma, \sigma\nu, \dots, \sigma\nu^{l-1}$, and $M_{d,l} = \mathrm{GL}_d(k)^l$ is the Levi subgroup of $\mathrm{GL}_{ld}(k)$ with $l$ equal blocks.

### The two classical inputs

Two facts on two cuspidal representations come from the theory of Bernstein and Zelevinsky.

**Theorem 2.7.2 (Irreducibility of a pair).** Let $x, y$ be irreducible cuspidal representations of $\mathrm{GL}_{d}(k)$ and $\mathrm{GL}_{d'}(k)$ with $y \not\cong x\nu$ and $x \not\cong y\nu$. Then $x \times y$ is irreducible.

This is (I. N. Bernstein and A. V. Zelevinsky, *Induced representations of reductive p-adic groups I*, Ann. Sci. ÉNS 10 (1977), §4). Here it is a proved input of the argument below.

**Theorem 2.7.3 (Reducibility of $\sigma \times \sigma\nu$).** Let $y$ be an irreducible cuspidal representation of $\mathrm{GL}_d(k)$ with $d \geq 1$. Then $y \times y\nu$ is reducible.

Lean: `CompanionTheory.RgGu.NR.redClC`.

**Remark 2.7.4 (Lean form of the reducibility).** The classical source is the same paper, §4, where the reducibility points of $\sigma \times \sigma\nu^{s}$ are found to be $s = \pm 1$. The Lean statement is the reducibility at $s = 1$ only, for one fixed field $k$, with the total size $2d$ carried as a separate equation. The proof below is a different argument, through complementary series.

*Proof.* Every irreducible cuspidal $y$ is $\rho \nu^z$ with $\rho$ unitary cuspidal and $z \in \mathbb{R}$: the central character of $y$ has a real exponent, and twisting by $\nu^{-z}$ makes it unitary, and a cuspidal representation with unitary central character is unitarisable, because its matrix coefficients are compactly supported modulo the centre.

Next, for unitary cuspidal $\rho$ there is $s \geq 0$ with $\rho\nu^{-s} \times \rho\nu^{s}$ reducible. Suppose not. The representations $F(s) = \rho\nu^{-s} \times \rho\nu^{s}$, $s \geq 0$, can be realised on one space (the compact picture), with the action of a compact open subgroup $K_0$ independent of $s$ and with matrix entries that are finite sums of exponentials $e^{r s}$. Each $F(s)$ is admissible and irreducible by assumption, and has a nonzero invariant Hermitian form, because its complex conjugate is isomorphic to its contragredient (for unitary $\rho$ the conjugate of $\rho\nu^{s}$ is the contragredient of $\rho\nu^{-s}$, and induction commutes with both operations). At $s = 0$ the representation is unitarily induced, so it is unitary. On each $K_0$-type the invariant form depends continuously on $s$, is unique up to a scalar, and cannot change signature without degenerating, which irreducibility forbids. So $F(s)$ is unitarisable for every $s \geq 0$. But a unitarisable induced representation satisfies a bound on the central exponents: if $t \in k^\times$ with $|t| \leq 1$ and the scalar matrix $t$ in the first block acts on the inducing data by $c$, then $|c| \cdot |t|^{d^2/2} \leq 1$. For $F(s)$ one has $|c| = |t|^{-ds}$ up to a unitary factor, and the bound fails for large $s$. This contradiction gives $s$.

By the irreducibility of a pair, $\rho\nu^{-s} \times \rho\nu^{s}$ can only be reducible if $\rho\nu^{s} \cong \rho\nu^{-s+1}$ or $\rho\nu^{-s} \cong \rho\nu^{s+1}$. Twists $\rho\nu^a$ and $\rho\nu^b$ with $a, b$ real are isomorphic only if $a = b$, by the central character. So $s = -s + 1$, that is $s = \tfrac12$ (the other case gives $s = -\tfrac12 < 0$). Twisting by $\nu^{-(z + 1/2)}$, which preserves irreducibility, turns $y \times y\nu = \rho\nu^{z} \times \rho\nu^{z+1}$ into $\rho\nu^{-1/2} \times \rho\nu^{1/2}$, which is reducible. $\square$

**Corollary 2.7.5 (Pairs, for all fields).** For every nonarchimedean local field $k$, every $d \geq 1$ and every irreducible cuspidal $\sigma$ of $\mathrm{GL}_d(k)$, the representation $\sigma \times \sigma\nu$ of $\mathrm{GL}_{2d}(k)$ is not irreducible.

Lean: `CompanionTheory.RgGu.NR.rhoNuRhoReducibleC`.

*Proof.* This is the theorem, restated with the induction written through the block decomposition $\mathrm{GL}_d \times \mathrm{GL}_d \subseteq \mathrm{GL}_{2d}$. $\square$

### The segment representation

The classical statement is the following (A. V. Zelevinsky, *Induced representations of reductive p-adic groups II*, Ann. Sci. ÉNS 13 (1980), §3). For a segment $\Delta = [\sigma, \sigma\nu^{l-1}]$, the representation $\sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$ has a unique irreducible subrepresentation $\langle \Delta \rangle$, and $r_{M_{d,l}}(\langle \Delta \rangle) = \sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}$.

**Theorem 2.7.6 (Segment representation).** Let $k$ be a nonarchimedean local field, $d, l \geq 1$, and $\sigma$ an irreducible cuspidal representation of $\mathrm{GL}_d(k)$. Let $I = \sigma \times \sigma\nu \times \dots \times \sigma\nu^{l-1}$. Then $I$ has an irreducible subrepresentation $S$, every irreducible subrepresentation of $I$ equals $S$, and
$$r_{M_{d,l}}(S) \cong \sigma \otimes \sigma\nu \otimes \dots \otimes \sigma\nu^{l-1}.$$

Lean: `CompanionTheory.RgGu.segmentRepresentation`.

**Remark 2.7.7 (Lean form of the segment theorem).** The Lean statement agrees with Zelevinsky's, with uniqueness as equality of subspaces of $I$ and the Jacquet module taken for the Levi subgroup with $l$ equal blocks. It does not name the representation or state its properties beyond these three.

*Proof.* Write $\tau_w = \sigma\nu^{w(0)} \otimes \dots \otimes \sigma\nu^{w(l-1)}$ for a permutation $w$ of $\{0, \dots, l-1\}$, and $\tau = \tau_1$.

*Step 1: the Jacquet module of $I$.* By the geometric lemma (Bernstein-Zelevinsky, §2, (2.12)), $r_{M_{d,l}}(I)$ has a filtration whose subquotients are the $\tau_w$, one for each $w$; the other terms vanish because $\sigma$ is cuspidal. The exponents $0, \dots, l-1$ are distinct, so the $\tau_w$ are pairwise non-isomorphic and each occurs exactly once as a composition factor. Each $\tau_w$ is irreducible, as a tensor product of irreducible smooth representations of the factors (Schur's lemma holds for each factor).

*Step 2: a unique irreducible subrepresentation.* $I$ has finite length, so it has an irreducible subrepresentation $S$. By Frobenius reciprocity, $\mathrm{Hom}(S, I) = \mathrm{Hom}(r(S), \tau)$, so $\tau$ is a quotient of $r(S)$. Since $\tau$ occurs once in $r(I)$ and $r$ is exact, two different irreducible subrepresentations would give two copies. So $S$ is the only one, and $\tau$ has multiplicity one in $r(S)$.

*Step 3: the case $l = 2$.* The composition factors of $r(S)$ are among $\tau$ and $\tau_{(01)} = \sigma\nu \otimes \sigma$. If $\tau_{(01)}$ occurred in $r(S)$, then $r(S)$ would contain both composition factors of $r(I)$, and $r(I/S) = 0$ by exactness. Every nonzero subquotient of $I$ has a nonzero Jacquet module for $M_{d,2}$, because its irreducible subquotients have cuspidal support on $M_{d,2}$. So $I = S$ would be irreducible, contrary to the corollary on pairs. Hence $r(S) \cong \tau$.

*Step 4: general $l$.* For each $i$ with $i + 1 < l$, induce from the Levi subgroup in which the blocks $i$ and $i+1$ are merged, using the segment representation of length $2$ from step 3 in that block. This gives a nonzero subrepresentation $T_i \subseteq I$, by transitivity of induction, such that every irreducible subquotient $\tau_w$ of $r(T_i)$ has $w^{-1}(i) < w^{-1}(i+1)$: the factor $\sigma\nu^{i}$ comes before $\sigma\nu^{i+1}$. The unique irreducible subrepresentation $S$ lies in every $T_i$. So every $\tau_w$ in $r(S)$ satisfies all these inequalities, hence $w = 1$. With multiplicity one from step 2, $r(S) \cong \tau$. $\square$

**Remark 2.7.8 (Formalization).** These are statements about $p$-adic groups, but the modules sit in a folder of real groups whose name refers to the archimedean place ([SegmentRepresentation.lean](lean:CompanionTheory/RealGroups/GeneralUnitaryRepresentations/ArchimedeanJacquetSegments/SegmentSubquotients/SegmentRepresentation.lean#L9)). Several proofs raise the elaboration limits, up to two million units for the reducibility step ([SomeRed.lean](lean:CompanionTheory/RealGroups/GeneralUnitaryRepresentations/ArchimedeanJacquetSegments/SomeRed.lean#L112)). Representations carry no topology: smoothness is a separate condition, and the geometric lemma is derived from a filtration result together with a finiteness theorem of Bernstein and Zelevinsky.
