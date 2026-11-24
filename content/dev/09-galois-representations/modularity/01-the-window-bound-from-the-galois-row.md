---
title: The window bound from the Galois row
decls:
  - UpperTheory.One.vwin_of_row
  - UpperTheory.One.Join.automorphic_window_of_inputs
  - UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm
  - UpperTheory.V.v_window_of_literal_automorphy_n
  - UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd
  - UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The window bound from the Galois row

This section proves that the [Galois row](/proof/galois-row/) gives the [window bound](/proof/vwin/). The proof is a chain of five reductions. Each reduction adds one package of inputs: the base change theorem for unitary groups, the published statements on CM abelian varieties, the published statements on $\mathrm{GL}_n$ and on Galois cohomology, and the extended hypotheses on Hilbert and quaternionic forms. The last reduction splits the bound into Lemma K and four case counts. The first count needs the vanishing of Sections 2 to 6, the second and third counts need the symplectic seed of Section 7 and the induction of Sections 8 and 9. The result is used by the step that proves the window bound for [every character of the row](/step/every-character-of-row/). The background on [Selmer and Tate-Shafarevich groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups) and on [the Galois representation of an automorphic representation](/learn/galois-representations/#the-galois-representation-of-an-automorphic-representation) is in Volume 1.

### The window bound

Let $\psi$ be a primitive Dirichlet character of conductor $N_\psi$. For an integer $e \geq 0$ and primes $q, d$, a number field $E$ is a *$\psi$-field for $(e, q, d)$* if there are $N \geq 1$, an embedding $E \to \mathbb{Q}(\zeta_N)$ and a primitive root of unity $\zeta$ of order $N$ with these properties: $2^{e+2}$, $N_\psi$, $q$ and $d$ divide $N$; and an automorphism $\tau$ with $\tau\zeta = \zeta^a$ fixes $E$ if and only if $a \equiv \pm 1 \pmod{2^{e+2}}$, $\psi(a) = 1$ and the [[Jacobi symbols|0ADTQBXRMC]] $(a/q)$ and $(a/d)$ are $1$. So $E$ is an abelian field inside a [[cyclotomic field|NN77VYSGXR]].

For a number field $E$, a prime $l$ and $e \geq 1$, let $\ell_l(E, e)$ be the [[length|CZSCNZH8VY]] of the $l$-primary [[Tate-Shafarevich group|BK9WBMF56G]] of the $e$-th twist of $\mathbb{Q}_l/\mathbb{Z}_l$ over $E$, for a fixed choice of local data at each prime.

**Definition 8.1.1 (Window pair).** Let $\varepsilon > 0$ and $Y > 1$. A pair of primes $(q, d)$ is a *window pair* at height $Y$ if $q \equiv 3 \pmod 8$, $d \equiv 7 \pmod{16}$, $q$ divides $d + 1$, every odd prime $p \leq Y^{\varepsilon/5}$ divides $d + 1$, and
$$\tfrac12 Y^{\varepsilon/5} < \log q \leq Y^{\varepsilon/5}, \qquad \tfrac12 L < \log d \leq L, \quad L = Y^{\varepsilon/5} (\log Y)^2.$$

**Definition 8.1.2 (Window bound).** The *window bound* holds for $\psi$ with constant $C$ if the following is true. Let $0 < \varepsilon < 1/52$, and let $e$ be a function from the reals to the integers with $x^{2 + 8\varepsilon} \leq 2^{e(x)} \leq 2 x^{2 + 8\varepsilon}$ for $x \geq 1$. Then there are $J \geq 1$ and $X_0$ such that for each $X \geq X_0$ and each window pair $(q, d)$ at height $X^{1/J}$ there is $Y$ with $X^{1/J} \leq Y$ and $Y^2 \leq X$, with this property. For each $x \in [Y, Y^2]$, put $t = \lfloor x^C \rfloor$. For each $\psi$-field $E$ for $(e(x), q, d)$ and each choice of local data, the lengths $\ell_l(E, e')$ are finite for $0 < e' < t$, and for each finite set $S$ of primes
$$\sum_{l \in S} \log l \sum_{e'=1}^{t-1} \ell_l(E, e') \leq \sqrt{\exp(x^{\varepsilon})}.$$
The *window bound* is the statement that this holds for every primitive $\psi$ with $C = 401$.

Lean: `UpperTheory.Top.VWin`.

### The inputs

The chain uses five packages. We state them in words. Their full statements are in the [proof of the window bound](/proof/vwin/) and in the steps that we link.

The *Galois row* is the statement of the step [the row](/step/row0b-def/): each regular algebraic polarized cuspidal representation of $\mathrm{GL}_n$ over a CM field has a Galois representation, compatible at each place with a [local Langlands map](/step/is-rect-def/) that satisfies a fixed list of laws.

**Theorem 8.1.3 (Base change for unitary groups).** Let $E$ be a CM field that is unramified over its maximal totally real subfield at all finite places. Each automorphic representation of a unitary group over that subfield, split by $E$, has a base change to $\mathrm{GL}_n$ over $E$ that is an isobaric sum of cuspidal pieces of sizes $N_1 + \dots + N_c = n$. This is proved in the step [base change](/step/base-change-n/), from Labesse's stabilization of the twisted trace formula; see [the twisted trace formula and base change](/learn/trace-formula/#the-twisted-trace-formula-and-base-change).

The *CM inputs* are eleven published statements on CM abelian varieties and Hecke L-functions: the Grothendieck deformation theorem, de Rham and crystalline cohomology of abelian varieties and their duals, the period comparison, Gauss-Manin periods, the Serre-Tate good reduction theorem, the main theorem of complex multiplication, the $j$-invariant and the Hilbert class field, the Siegel-Klingen and Deligne-Ribet rationality, and the functional equations of partial zeta functions and of Hecke-Tate L-functions. They are proved in the step [CM and abelian inputs](/step/cm-abelian-inputs-from-literature/).

The *rank $n$ package* has four parts: eighteen local statements on $\mathrm{GL}_n$ of a local field (finiteness, the Langlands classification, the local converse theorem, depth zero induction and others), fifteen global automorphy statements (two of them are the base change theorem and the Galois row), twelve statements on Galois cohomology (Poitou-Tate duality, local finiteness, local Tate duality, Euler characteristics, the Greenberg-Wiles formula and Bloch-Kato), and the CM inputs. See [the published inputs](/proof/literature/).

The *extended hypotheses* keep the rank $n$ package and add Clozel's statements on cohomological representations, Galois representations for totally real fields in rank 2, strong multiplicity one, quadratic and cyclic base change for $\mathrm{GL}_2$, newforms, a weak descent statement, cyclotomic statements and the existence of a definite quaternion algebra. They come from the rank $n$ package by [the patching theorem for the published hypotheses](/entry/published-hypotheses-from-patching-alt/).

### Lemma K and the counts

**Definition 8.1.4 (Lemma K).** Let $C_K > 0$. *Lemma K holds with constant $C_K$* if for each prime $l$, each totally complex number field $L$ of degree $n$ and discriminant $D$ that contains a primitive root of unity of order $l$ (of order $4$ if $l = 2$), and each $e \geq 1$, the group $H^2$ of $L$ with coefficients $\mathbb{Z}_l$ twisted by the $(e+1)$-th power of the cyclotomic character is finite and
$$\log \# H^2 \leq \exp\bigl((2en)^{C_K} \log(2D)\bigr).$$

The counts live on a *host*: a primitive character $\chi$ of conductor $q$, an exponent at least $2$ and primes $q_1 \equiv 3 \pmod 8$ and $d \equiv 7 \pmod{16}$ prime to $q$, with modulus $N = \mathrm{lcm}(2^{\mathrm{ex}+2}, q)\, q_1 d$. For a Dirichlet character $\psi$ modulo $N$ with $\psi(-1) = (-1)^e$ there is a Tate-Shafarevich length of the twist of $\mathbb{Q}_l/\mathbb{Z}_l$ by $\psi^{-1}\chi^{-e}$ over $\mathbb{Q}$. A prime $l$ falls in one of the cases I, II, III, IV, V or Z, which are conditions on $l$, $e$ and $\psi$.

**Definition 8.1.5 (Case count).** For a case $P$, the *count for $P$* holds if for each $\chi$ there is $C$ such that for each host of $\chi$ with large enough primes, each odd prime $l$, each $0 < e < t$ and each $\psi$ in case $P$, the length is at most $(l N e)^C$. The counts II, III and V have this form. Count I bounds the sum over the primes $l$ in case I of $\log l$ times the sum of the lengths over $\psi$ by $(N t)^C$.

### The chain

**Theorem 8.1.6 (Window bound from the extended hypotheses).** Assume the extended hypotheses. Then the window bound holds.

Lean: `UpperTheory.V.HV.DescentVanishingReductions.vwin_of_hypotheses_H_E_alt`.

*Proof.* We prove the four counts and Lemma K, and then we add the other parts of the bound.

Step 1. From the rank $n$ package, [Lemma K holds](/entry/lemma-k-lit-n-alt/) with some constant $C_K$.

Step 2. From the extended hypotheses we get the two facts on unitary three-dimensional representations that the later sections prove: an end statement for the residual images and a core statement for case V.

Step 3. The extended hypotheses give [the symplectic image statement](/entry/sp4-in0-alt/) of Section 7: in the cases II and III, each good datum is finite, has no end and all its irreducible pieces are automorphic of dimension four. With Lemma K this gives [the counts II and III](/entry/count-ii-and-count-iii-of-prints-h-of-sp4-in/).

Step 4. The extended hypotheses give [Kato's vanishing for two twists](/entry/kato-two-w-of-prints-h/) of Section 2. The rank $n$ package and the end statement of Step 2 give automorphy of unramified representations. With Lemma K these give [the count I](/entry/count-i-of-printed-bound-k-kato-automorphy/).

Step 5. Lemma K and the core statement of Step 2 give [the count V](/entry/count-v-of-printed-bound-k-reduced-unitary-lift/).

Step 6. The length of the Tate-Shafarevich group splits into three parts: the prime $l = 2$, and for odd $l$ the two eigenspaces of complex conjugation. Lemma K, Poitou-Tate duality, local finiteness, local Tate duality and the theorem of Ferrero and Washington (Ann. of Math. 109, 1979, on the vanishing of the $\mu$-invariant of cyclotomic $\mathbb{Z}_p$-extensions of abelian fields) bound the part at $l = 2$ and the parts over the cyclotomic layers. A separate bound covers the minus part for each CM field of the family. The case Z count holds since the length is zero for the trivial character when $l \geq 5$, $e \geq 2$ is even and $l - 1$ divides $2e$. These bounds and the four counts give the window bound, as in Steps 6 and 7 of the [proof of the window bound](/proof/vwin/). $\square$

**Theorem 8.1.7 (Window bound from the rank $n$ package).** Assume the rank $n$ package. Then the window bound holds.

Lean: `UpperTheory.V.HV.DescentVanishingReductions.v_window_of_automorphy_csd_ss_mono_odd` (also `UpperTheory.V.v_window_of_literal_automorphy_n`, a second name).

*Proof.* The rank $n$ package and the weak descent statement give the extended hypotheses, by [the patching theorem for the published hypotheses](/entry/published-hypotheses-from-patching-alt/). Then this is Theorem (Window bound from the extended hypotheses) applied to them. $\square$

**Theorem 8.1.8 (Window bound from four packages).** Assume the open image condition (the Galois row), the base change theorem for unitary groups, the Galois row and the CM inputs. Then the window bound holds.

Lean: `UpperTheory.One.Join.v_window_of_depth_zero_residual_bc_cm`.

*Proof.* The local statements and the statements on Galois cohomology are published theorems, and the open image condition passes them on. The fifteen global statements come from the base change theorem, the Galois row and published theorems. With the CM inputs this is the rank $n$ package. So this is Theorem (Window bound from the rank $n$ package) applied to it. $\square$

**Theorem 8.1.9 (Window bound from the inputs).** Assume the open image condition, the base change theorem for unitary groups and the Galois row. Then the window bound holds.

Lean: `UpperTheory.One.Join.automorphic_window_of_inputs`.

*Proof.* The CM inputs are proved in the step [CM and abelian inputs](/step/cm-abelian-inputs-from-literature/). This is Theorem (Window bound from four packages) applied to the three inputs and the CM inputs. $\square$

**Theorem 8.1.10 (Window bound from the row).** Assume the Galois row. Then the window bound holds.

Lean: `UpperTheory.One.vwin_of_row`.

*Proof.* The open image condition is the Galois row. The base change theorem for unitary groups is proved. This is Theorem (Window bound from the inputs) applied to the row, the base change theorem and the row. $\square$

**Remark 8.1.11 (Formalization).** The open image condition is a structure with one field, and that field is the Galois row itself ([TemperedProductOfSquareIntegrable.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean#L207)). So the first theorem passes the row twice ([VwinOfRow.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean#L5)). The CM inputs are built by lemmas with names that end in `_of_open`, which take the open image condition and do not use it; for example `elliptic_main_theorem_cm_of_open` is `PositivityTheory.Prw.ellipticMainTheoremCM_holds` ([TemperedProductOfSquareIntegrable.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean#L209)), and the builder is at [TopMainZj.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean#L59). The name `v_window_of_automorphy_csd_ss_mono_odd` does not describe its statement, and `v_window_of_literal_automorphy_n` is a second name of it ([WindowBoundOfLiteratureLevel.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/WindowBoundOfLiteratureLevel.lean#L33)). That file and TopMainZj.lean set `maxHeartbeats 800000` for proofs of a few terms. Step 2 of the main proof is `ends0_alt`, and Step 6 is `UpperTheory.V.HV.Core.of_four_alt`, which a later section proves. The length $\ell_l(E,e)$ is `Formalism.GaloisCohomology.shaLen` of a local datum; this section does not unfold it, nor the Galois row, the cases I to Z or the fields of the packages.
