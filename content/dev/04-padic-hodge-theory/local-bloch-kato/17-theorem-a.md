---
title: Theorem A
decls:
  - GlobalTheory.TheoremAFinal.integralityFromMetric_of_le
  - GlobalTheory.T.integralityFromMetric_of_160_le
  - GlobalTheory.theoremA_closing
  - GlobalTheory.T.localLifting_of_blochKato_tateDuality_eulerChar
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem A

This section proves Theorem A, a bound on the congruence length of a surjection of crystalline lattices whose Hodge-Tate jumps lie in deep windows. The first theorem deduces Theorem A with any constant $C \ge 160$ from the admitted local statements and three facts on Wach modules and de Rham spaces. The second theorem supplies the admitted statements from the Bloch-Kato formula, local Tate duality and the Euler characteristic formula. Theorem A with constant $160$ is used in [the bound at twisted places](/entry/twisted-place-bound-closing/).

We keep the notation of Section 7: $\mathrm{col}(F)$ is the congruence length of a lattice map $F : T_1 \to T_2$, and $\mathrm{col}(F) \le x$ relative to $\ell$ means $\mathrm{col}(F) \le x\, \mathrm{length}_{\mathcal{O}}(\mathcal{O}/\ell)$. Let $\ell$ be a prime and $K$, $L$ finite extensions of $\mathbb{Q}_\ell$, with $K_0$ the maximal unramified subfield of $K$. Put $n = [K_0 : \mathbb{Q}_\ell]$ and $e = [K : K_0]$. For an embedding $\tau : K \to L$ and an integer $a$, $\mathrm{mult}_\tau(T, a)$ is the multiplicity of $a$ as a Hodge-Tate jump of $T$ at $\tau$.

**Definition 7.17.1 (Good pair).** For $s \ge 1$, the pair $(K, L)$ is *good with level $s$* if $\ell \ne 2$ or $s \ge 2$, $K$ lies in the field $K_s$ of level $s$ over $K_0$, and every $\mathbb{Q}_\ell$-embedding of $K_s$ into $\overline{\mathbb{Q}}_\ell$ has image in $L$. We do not unfold $K_s$.

So $(K, L)$ is in Case A exactly when $K$ is unramified, $\ell \ne 2$, and $(K, L)$ is good with level $1$.

**Definition 7.17.2 (Deep windows and the bound of Theorem A).** For a sign $\mathrm{up} \in \{\text{true}, \text{false}\}$ and $b, S \ge 0$, the *deep window* is $[b, b + S]$ if $\mathrm{up}$ is true and $[-b - S, -b]$ if not. For $C \in \mathbb{R}$ and $r, S, \eta, m, h \ge 0$ put
$$A_C = C(ne + 1)\, r \Big(\frac{e h}{\ell} + e S + e \log_\ell h + 1 + \eta\Big) + n e (e + 1)\, m\, C (h + 1).$$

**Definition 7.17.3 (Theorem A with constant $C$).** *Theorem A with constant $C$* at $(K, L)$ is the following statement. Let $F : T_1 \to T_2$ be a map of crystalline $\mathcal{O}$-lattices of $G_K$ that is onto, and let $r$ be the dimension over $L$ of the space of $T_2$. Let $S, \eta, m, h \ge 0$, and for each embedding $\tau : K \to L$ let $\mathrm{up}(\tau)$ be a sign and $b(\tau) \ge 0$. Assume:

1. at every $\tau$, the jumps of $T_1$ lie in the deep window of $(\mathrm{up}(\tau), b(\tau), S)$ or in $[-\eta, \eta]$;
2. $\eta < b(\tau)$ for every $\tau$;
3. at every $\tau$, $\sum_{a = -\eta}^{\eta} \mathrm{mult}_\tau(T_2, a) \le m$;
4. at every $\tau$, the jumps of $T_1$ lie in $[-h, h]$;
5. either $e = 2$, or $\mathrm{up}(\tau) = \mathrm{up}(\tau')$ whenever $\tau$ and $\tau'$ agree on $K_0$.

Then $\mathrm{col}(F) \le A_C$ relative to $\ell$.

*Theorem A with constant $C$* for local data is this statement at every prime $\ell \ne 2$ and every pair $(K, L)$ that is good with level $1$.

The constants $C_A, C_B, C_K$ below enter only through the admitted statements: one of them is the lifting theorem in all cases with these constants. We do not unfold the admitted statements.

**Theorem 7.17.4 (Theorem A from the admitted statements).** Let $D$ be the data of the series and $H$, $F$, $C_m$ local data over $D$, as in Section 5. Let $C_A, C_B, C_K \in \mathbb{R}$ and $C \ge 160$. If the admitted statements of Theorem A hold for $(C_A, C_B, C_K)$, then Theorem A with constant $C$ holds for the local data.

Lean: `GlobalTheory.TheoremAFinal.integralityFromMetric_of_le` (also `GlobalTheory.T.integralityFromMetric_of_160_le`, a second name).

*Proof.* By [the theorem with a large constant](/entry/integrality-from-metric-of-large-constant/), which is proved from [the uniform link](/entry/lifting-theorem-of-uniform-link/), the statement holds for $C \ge 160$ once three facts are known for the local data. We check them.

*Exactness of the Wach functor.* Let $(K, L)$ be good with level $s$, and let $0 \to T_0 \xrightarrow{\iota} T_1 \xrightarrow{\pi} T_2 \to 0$ be a short exact sequence of lattices of $G_K$. Then the Wach functor $W$ of the local data at $(K, s, L)$ sends it to an exact sequence: $W(\iota)$ is injective, $W(\pi)$ is surjective, and the kernel of $W(\pi)$ is the image of $W(\iota)$. A lemma on the étale functor gives this.

*Full de Rham spaces.* Let $(K, L)$ be good with some level, and let $T$ be a crystalline lattice of $G_K$ in a space $V$. Then for every embedding $\tau : K \to L$, the $\tau$-part $D_{\mathrm{dR}, \tau}(T)$ has dimension $\dim_L V$ over $L$. A lemma on crystalline lattices gives this.

*Full rank of the invariant parts.* Let $(K, L)$ be good with level $1$, and let $T$ be a crystalline lattice of $G_K$ in a space $V$. Then for every letter $c \in \mathbb{Z}/n$, the $\Delta$-invariant part of the Wach module of $T$ at $c$ has dimension $\dim_L V$ over $L$. A lemma on letters gives this.

With these three facts, the theorem with a large constant gives Theorem A with constant $C$. $\square$

The proof holds for every choice of $(C_A, C_B, C_K)$. The bound $A_C$ does not depend on them; only the admitted statements do.

**Theorem 7.17.5 (Theorem A).** Assume the Bloch-Kato dimension formula, local Tate duality and the local Euler characteristic formula, as stated in Section 4. Let $D$ be the data of the series and $H$, $F$, $C_m$ local data over $D$, and let $C \ge 160$. Then Theorem A with constant $C$ holds for the local data.

Lean: `GlobalTheory.theoremA_closing` (also `GlobalTheory.T.localLifting_of_blochKato_tateDuality_eulerChar`, a second name).

*Proof.* From the three published inputs, a theorem on the admitted statements gives the admitted statements of Theorem A for the constants $(C_A, C_B, C_K) = (23, 32, 32)$. Then [Theorem A from the admitted statements](/entry/integrality-from-metric-of-le/) applies with these constants and $C$. $\square$

**Remark 7.17.6 (Formalization).** In Lean, Theorem A with constant $C$ at $(K, L)$ is `thmA`, and $A_C$ is `boundA`. The family version is `Conclusion1 D C`, which unfolds to `TheoremBLocal D.loc C` ([ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L51)): the name says Theorem B, but the content is Theorem A. The statement of the first theorem is `IntegralityFromMetric D HW F Cm CA CB CK C`, which is `Adm1 D HW F Cm CA CB CK → Conclusion1 D C` (line 161); neither a metric nor integrality appears in it. The three facts are `FontExAll`, `DdRFull` and `DiRank`; `FontExAll` has an unused argument `_F` ([FontExAll.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FontExAll.lean#L10)), and `DiRank` has unused arguments `_F` and `_Cm` ([DdRFull.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DdRFull.lean#L14)). They are proved by `GlobalTheory.LatExact.W_exact`, `GlobalTheory.CrysDdR.finrank_DdRE_of_isCrys` and `GlobalTheory.NL.IotaLetterRank.finrank_iota_letter` ([LocalLiftingOfEtaleExactDeRhamCrystallineConst.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingOfEtaleExactDeRhamCrystallineConst.lean#L16)), which we read only through their statements. The admitted statements for $(23, 32, 32)$ come from `GlobalTheory.T.localLifting_theoremA_hypotheses_admitted` ([LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalLiftingTheoremAOfBlochKatoTateDualityEulerC.lean#L16)). The definition of a good pair is `Good` ([DataNLoc.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/DataNLoc.lean#L477)). The second names are one-line wrappers.
