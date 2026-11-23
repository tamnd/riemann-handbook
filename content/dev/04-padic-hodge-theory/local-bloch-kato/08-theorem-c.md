---
title: Theorem C
decls:
  - GlobalTheory.T.ramified_coefficient_chains_of_hypotheses
  - GlobalTheory.theoremC_of_admitted_inputs
  - GlobalTheory.T.prv_twenty_five_of_blochKato_tateDuality_eulerChar
  - GlobalTheory.ramifiedCoefficientChains_prv_twenty_five
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem C

Theorem C is a second bound on congruence lengths, for an even number of letters and Hodge-Tate weights in windows whose sign changes from letter to letter. It also gives a bound on the lifting exponent, and when $T_2$ has no small weights it shows that the map lifts with an explicit exponent. This section proves Theorem C with the constant $C = 25$, first from a list of admitted statements and four inputs, and then for the local data of the series. The result is used in [the inert step](/entry/inert-step-main-alt-alt/).

We keep the notation of Sections 6 and 7: the congruence length $\mathrm{col}(F)$ of a lattice map, the bound relative to $\ell$, lifting with an exponent, the jump statement, Fontaine's inequality and the letter condition. Let $n$ be the number of letters of the Wach data at $(K, L)$.

**Definition 7.8.1 (Windows and constants).** For integers $d, S, \eta \ge 0$ and $b_i \ge 0$ for each letter $i$, the *window* at $i$ is
$$W_d(i) = \begin{cases} [-(b_i + S), -b_i] \cup [-\eta, \eta] & \text{if } i + d \text{ is even}, \\ [b_i, b_i + S] \cup [-\eta, \eta] & \text{if } i + d \text{ is odd}, \end{cases}$$
where $i$ is read as an integer in $[0, n)$. Put $\hat h = \max_i b_i + S$ and, for a prime $\ell$ and $H \ge 0$,
$$\lambda(H) = \log_\ell(2H) + 1, \qquad a(H) = \frac{H(2\ell - 1)}{(\ell - 1)^2} + 3 + \lambda(H), \qquad c(H) = \frac{H + 1}{\ell - 1} + 1.$$
For constants $k_1, \dots, k_5$ and $C$, put
$$\epsilon(H) = \frac{k_1 H}{\ell^2} + k_2 S + \frac{k_3 \eta}{\ell - 1} + C\lambda(H),$$
$$\mathrm{bd}(e, e') = (n + 1) r e + k_4 n m e' + k_5 n \big(rS + 2m\, c(H)\big),$$
where $r$ and $m$ are the integers of the setting below. The *lifting exponent* $e'_d$ is the exponent $2\epsilon_W + \epsilon_U$ of Section 7, formed with the bounds $M_i = b_i + S$, $h_i = \eta$ when $i + d$ is even and $M_i = \eta$, $h_i = b_i + S$ when $i + d$ is odd.

**Definition 7.8.2 (Setting of Theorem C).** A lattice map $F : T_1 \to T_2$ is in the *setting of Theorem C* for $d$, $b$, $S$, $\eta$ and $m$ if:

1. $(K, L)$ is in Case A, $\ell \ge 11$ and $n$ is even;
2. $\mathcal{O}$ is a discrete valuation ring with fraction field $L$, and $L$ contains a primitive $\ell$-th root of unity;
3. $T_1$ and $T_2$ are crystalline and $F$ is surjective;
4. at every letter $i$ and every embedding $\tau$ over $\tau_i$, the jumps of $T_1$ at $\tau$ lie in $W_d(i)$;
5. at every such $\tau$, the number of jumps of $T_2$ at $\tau$ in $[-\eta, \eta]$, with multiplicity, is at most $m$;
6. $2a(\hat h + \eta) + \eta + 1 \le b_i$ and $\hat h / 2 \le b_i$ for every letter $i$.

**Definition 7.8.3 (Theorem C).** *Theorem C with constants $k_1, \dots, k_5$ and $C$* at $(K, L)$ is the statement: for every $F : T_1 \to T_2$ in the setting of Theorem C for some $d$, $b$, $S$, $\eta$, $m$, with $r$ the dimension over $L$ of the space of $T_2$ and $H = \hat h + \eta$, there is an integer $e \le \epsilon(H)$ such that, relative to $\ell$,
$$\mathrm{col}(F) \le \mathrm{bd}(e, e'_d),$$
and, if $m = 0$, $F$ lifts with exponent $e + 3S$. *Theorem C with constant $C$* for local data is Theorem C with constants $(32, 4, 10, 4, 3/2)$ and $C$ at every prime $\ell$ and every good pair $(K, L)$, for the Wach data of $H_\ell$ at $(K, L)$.

**Definition 7.8.4 (Admitted statements of Theorem C).** For constants $(C_R, C_A, C_B, C_K)$ the *admitted statements of Theorem C* are 19 statements on the local data:

- statements 1 to 4: four properties of $\Delta$-invariant lattices, among them a global statement on these lattices and the semisimplicity of $\gamma$ on a quotient;
- statements 5 to 10: the eight local lifting statements of Section 6, with the constants $C_R$, $C_A$, $C_B$, $C_K$, grouped in six statements;
- statement 11: strict exactness of $D_{\mathrm{cris}}$ on sequences of crystalline representations, at every $(K, L)$;
- statement 12: a statement on Bloch-Kato classes;
- statement 13: a count of generators of $H^1_f$;
- statement 14: a further property of $\Delta$-invariant lattices;
- statement 15: the Bloch-Kato extension criterion;
- statement 16: a statement on Herr extensions;
- statement 17: two naturality statements for classes;
- statement 18: a statement on the letters of Wach modules;
- statement 19: the bound on the number of generators of $H^1_f$ of Section 6.

We do not unfold these statements.

**Theorem 7.8.5 (Theorem C from the admitted statements).** Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. Assume the jump statement, the letter condition, a naturality statement for Herr classes of extensions, Fontaine's inequality, and the Fontaine equivalence with $\psi$, for the local data. Then, for all constants $(C_R, C_A, C_B, C_K)$, if the admitted statements of Theorem C hold, Theorem C with constant 25 holds for the local data.

Lean: `GlobalTheory.T.ramified_coefficient_chains_of_hypotheses` (also `GlobalTheory.theoremC_of_admitted_inputs`).

*Proof.* Assume the admitted statements, and fix $\ell$, a good pair $(K, L)$ and $F : T_1 \to T_2$ in the setting of Theorem C for $d$, $b$, $S$, $\eta$, $m$. Call a letter $c$ *even* if $c + d$ is even. Let $I(F)$ be as in Section 7. The proof has three parts.

*Cocycles to Wach vectors.* There is an integer $s$, bounded in terms of $\ell$, $\hat h$, $\eta$ and $S$, with this property. For each finite free $\mathcal{O}$-module $P$ and each map $g$ from $P$ to the finite cocycles of $T_2$, there are a submodule $P_2 \subseteq P$, with $P_2 = P$ if $m = 0$, and for each even letter $c$ a map $w_c$ from $P_2$ to the Wach module $D(T_2)$, such that: $P_2$ has bounded index in $P$, measured by a chain condition with steps controlled by $m$ and the length of $\mathcal{O}/\ell$; and for each $f \in P_2$ there are cocycles $\kappa_c$, the cocycle that $w_c(f)$ defines at $c$, with $\ell^s g(f) \mp \sum_c \kappa_c$ a coboundary for one choice of sign. This part comes from local lemmas on Wach modules, whose proof uses the admitted statements, the jump statement, the naturality of Herr classes, Fontaine's inequality and the Fontaine equivalence.

*Chains of submodules.* There is an integer $e$, bounded in terms of $\ell$, $\hat h$, $\eta$ and $S$, with this property. For each even letter $c$ and each map $w$ from a submodule $P_2$ of a finite free module to $D(T_2)$ whose values satisfy a divisibility condition at $c$, there is a submodule $P' \subseteq P_2$ of bounded index such that for each $f \in P'$ and $j \ge 0$ some $u \in D(T_1)$ in the image part at $c$ satisfies: $\ell^{j + e} w(f) - F(u)$ lies in a small part of $D(T_2)$. If $m = 0$, the same holds for all $f \in P_2$ with $\ell^{j + e + 3S}$. This part comes from lifting lemmas for Frobenius, a bound on $H^2$, a dual lemma and its form at level 0, and lemmas on the action of $\gamma$ at the letters, which use the letter condition and the jump statement.

*Lifts.* If $u \in D(T_1)$ is in the image part at an even letter $c$, $\kappa$ is the cocycle that $w \in D(T_2)$ defines at $c$, and $\ell^k w - F(u)$ lies in the small part, then $\ell^k \kappa \in I(F)$. This follows from the admitted statements.

Put together, a power of $\ell$ with exponent bounded by $s + e$ (plus $j$) sends $g(f)$ into $I(F)$ for $f$ in a submodule of bounded index. With $g$ a map onto the finite cocycles, a count of lengths as in Section 7 gives an exponent at most $\epsilon(H)$ and $\mathrm{col}(F) \le \mathrm{bd}(e, e'_d)$ relative to $\ell$, with the constants $(32, 4, 10, 4, 3/2)$ and $C = 25$. For $m = 0$ the submodules are all of $P$, and the same argument shows that $F$ lifts with exponent $e + 3S$. We do not unfold the bounds on $s$ and $e$ or the final count. $\square$

**Theorem 7.8.6 (Theorem C for the local data).** Assume the theorem of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$. Then Theorem C with constant 25 holds for the local data.

Lean: `GlobalTheory.T.prv_twenty_five_of_blochKato_tateDuality_eulerChar` (also `GlobalTheory.ramifiedCoefficientChains_prv_twenty_five`).

*Proof.* The admitted statements of Theorem C hold with $(10, 23, 32, 32)$. Statements 1 to 4 are the used forms of the local conclusions on Wach modules, statements 5 to 10 are [the local lifting statements with fixed constants](/entry/local-constants-from-admitted-local-galois-statements-alt/), statement 11 is strict exactness of $D_{\mathrm{cris}}$, statement 12 follows from the Bloch-Kato formula at every local situation, statement 15 is the extension criterion of the tie, and the other statements come from the theory of Herr complexes and of the operator $\gamma - 1$ on the letters and from the bound on generators of $H^1_f$. The jump statement follows from the tie, as in Section 7. [The clauses on Wach lattices](/entry/wach-lattice-later-clauses-hold/) give the letter condition. The naturality of Herr classes holds for the local data, Fontaine's inequality holds, and the Fontaine functor is fully faithful and exact with an operator $\psi$. Now apply [Theorem C from the admitted statements](/entry/ramified-coefficient-chains-of-hypotheses/) with $(10, 23, 32, 32)$. $\square$

**Remark 7.8.7 (Formalization).** As in Section 6, the three published inputs go only to the local lifting statements, which ignore them, so Theorem C holds without them. The admitted statements of Theorem C are proved by a theorem with the same short name as the main theorem of Section 6, in a second namespace. The constant 25 is fixed in the statement of the first theorem, and the main Lean name of the second speaks of "prv twenty five", which is this constant. Theorem C for local data is stated with a range condition on $m$ that is always true, and its statement takes the Fontaine data $F$ as an argument that it does not use ([RamifiedCoefficientChains.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/RamifiedCoefficientChains.lean#L134)). Both main names are one-line wrappers that set `maxHeartbeats` to 1000000.
