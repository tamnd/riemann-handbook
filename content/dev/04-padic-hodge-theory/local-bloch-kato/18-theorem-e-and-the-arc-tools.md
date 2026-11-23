---
title: Theorem E, Corollary A and the arc tools
decls:
  - GlobalTheory.ThmECorA.closing
  - GlobalTheory.T.theoremE_corollaryA_closing_all_data
  - GlobalTheory.ArcTools.arc_tools_from_clauses
  - GlobalTheory.T.arcTheorem_tools_of_wachModuleConclusions
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem E, Corollary A and the arc tools

This section proves two results on Wach modules for the local data of the series. The first is Theorem E with constant $800$ together with Corollary A for all large constants. Theorem E gives an explicit exponent with which a surjection of crystalline lattices lifts, when the jumps of the source lie in windows fixed by an arc datum, and it bounds that exponent. Corollary A bounds the congruence length when the thick letters come in small clusters. The second result collects 13 statements on Wach modules, the *arc tools*, from the clauses on Wach lattices. Both results are inputs of the local lifting statements that the series uses.

We keep the notation of Section 6 for letters $i \in \mathbb{Z}/n$, the embeddings $\tau_i$, arc data, Wach modules and $\Delta$-invariant parts, and the notation of Section 7 for congruence lengths and exponents of lifting. For a lattice $T$, a letter $i$ and a set $X \subseteq \mathbb{Z}$, we say that the jumps of $T$ *at $i$ lie in $X$* if, at every embedding $\tau : K \to L$ that restricts to $\tau_i$ on $K_0$, the Hodge-Tate jumps of $T$ lie in $X$.

**Definition 7.18.1 (Windows of types).** Let $G, S, \eta \ge 0$. The *window* of a type is $[-G, G]$ for a thin type, $[b, b + S] \cup [-\eta, \eta]$ for the type up of size $b$, and $[-b - S, -b] \cup [-\eta, \eta]$ for the type down of size $b$. Put $g = \max(G, S, \eta, 1)$. For cuts with lengths $\mathrm{len}(c)$, let $\ell_{\max}$ be the largest length, and let $\rho(c)$ be the number of $0 \le s < \mathrm{len}(c)$ such that the letter $c - s$ is thick.

The *cut conditions* for $j$ are conditions 1 and 2 of a good arc datum in Section 6, the inequality $j \le \mathrm{len}(c)$ for every cut $c$, and the condition that the $j$ letters after each cut are thin.

**Definition 7.18.2 (The exponent of Theorem E).** Let $\ell \ge 5$, $j \ge 1$, $h \ge 0$, and let $H_1, H_2$ be functions on the letters. Put $M = \lfloor (h + 2g)/(\ell - 1) \rfloor + 1$ and
$$\sigma = \Big\lceil \Big(3g + \frac{M}{\ell^{j-1}}\Big) \frac{\ell}{(\ell - 1)^2} + 1 \Big\rceil.$$
There are numbers $\rho_{H}$, built from the values of $H_1$ and $H_2$ along the cuts, and $\kappa$, built from the $\ell$-adic valuations of jumps in windows of length at most $3g$ inside $[-2h, 2h + 1]$; we do not unfold them. The *initial exponent* is $\epsilon_0 = 2\sigma + \rho_H + 2 g \ell_{\max}$, and the *exponent of Theorem E* is
$$\epsilon = 2\rho_H + 4\sigma + 2\epsilon_0 + 2\kappa.$$

**Definition 7.18.3 (Theorem E with constant $C$).** *Theorem E with constant $C$* for local data has two parts.

The *lifting part* is the following statement, at every prime $\ell$, every pair $(K, L)$, every $n \ge 1$ and every family of embeddings $\tau_i : K_0 \to L$, $i \in \mathbb{Z}/n$. Assume that the $\tau_i$ are letters for the period data and that $\ell \ge 5$. Let $F : T_1 \to T_2$ be a map of crystalline lattices of $G_K$ that is onto, with good coefficients for $T_1$; we do not unfold letters and good coefficients. Let $j, G, S, \eta, h \ge 0$, types $\mathrm{ty}(i)$, cuts with lengths, and functions $M_1, h_1, M_2, h_2$ on the letters satisfy:

1. at each letter $i$, the jumps of $T_1$ lie in the window of $\mathrm{ty}(i)$;
2. the jumps of $T_1$ lie in $[-h, h]$, and $g \le h$;
3. every type is thin, or has size $b$ with $\eta < b$ and $b + S \le h$;
4. the cut conditions for $j$ hold, and $\rho(c) \le 2$ for every cut $c$;
5. at each letter $i$, the jumps of $T_k$ lie in $[-M_k(i), h_k(i)]$, for $k = 1, 2$;
6. a word condition on the types along each arc, which compares the sizes of an up letter and a later down letter with $\ell$ and with $\epsilon_0$; we do not unfold it.

Then $F$ lifts with the exponent $\epsilon$ of Theorem E for $(\ell, n, j, g, h, M_1 + h_1, M_2 + h_2)$ and the cuts.

The *bound part* is a statement on numbers only. Let $\ell \ge 5$ be a prime, and assume the cut conditions for $j$, $g \le h$, $H_k(i) \le 2h$ for all letters, and $H_k(c + k') \le 2G$ for each cut $c$ and $1 \le k' \le j$, for $k = 1, 2$. Then
$$\epsilon \le C\Big(\frac{h}{(\ell - 1)^{j+1}} + g\, \ell_{\max} + \log_\ell h\Big).$$

**Definition 7.18.4 (Corollary A with constant $C$).** Let $b, \eta \ge 0$ and sizes $\mathrm{sz}(i)$. A letter $i$ is *thick* if $b \le \mathrm{sz}(i) \le b + \eta$. The thick letters form *clusters of gap $j$* if for every thick letter $t$, either none of $t - 1, \dots, t - j$ is thick, or there is $1 \le d \le j$ such that $t - d$ is thick and $t - k$ is not thick for every other $1 \le k \le d + j$.

*Corollary A with constant $C$* is the following statement, at every $\ell$, $(K, L)$, $n$ and family $\tau_i$ as above. Assume that the $\tau_i$ are letters and $\ell \ge 11$. Let $F : T_1 \to T_2$ be a map of crystalline lattices of $G_K$ that is onto, with good coefficients for $T_1$, and let $r$ be the dimension over $L$ of the space of $T_2$. Let $b, w, S, \eta, j \ge 0$ with $1 \le j$ and $j + 1 \le n$, a sign $\mathrm{typ}(i)$ and a size $\mathrm{sz}(i)$ for each letter, such that:

1. at each letter $i$, the jumps of $T_1$ lie in the window, with $G = 0$, of the type up or down of size $\mathrm{sz}(i)$, according to $\mathrm{typ}(i)$;
2. every letter is thick or has size at most $w$;
3. $C(j + 1)(w + S + \eta + 1) \le b$;
4. the thick letters form clusters of gap $j$.

Put $h = b + \eta + S$ if some letter is thick and $h = w + S + \eta$ if not. Then, relative to $\ell$,
$$\mathrm{col}(F) \le C(n + 1)\, r \Big(\frac{h}{(\ell - 1)^{j+1}} + (w + S + \eta + 1)(j + 1) + \log_\ell h\Big).$$

**Theorem 7.18.5 (Theorem E and Corollary A).** Assume the Bloch-Kato dimension formula, local Tate duality and the local Euler characteristic formula. Then there is a constant $C_0$ such that for every family of local data, Theorem E with constant $800$ holds, and Corollary A with constant $C$ holds for every $C \ge C_0$.

Lean: `GlobalTheory.ThmECorA.closing` (also `GlobalTheory.T.theoremE_corollaryA_closing_all_data`, a second name).

*Proof.* Let $C_0$ be the constant of a theorem on the local corollary, which asserts that some constant works; we do not make it explicit. Fix local data. We collect five inputs.

1. For every $(K, L)$ in Case A, $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ for the period data at $K$, by a lemma on unramified fields.
2. The theorem of Fontaine and decompletion holds for the local data.
3. The Fontaine functor is fully faithful and exact, with an operator $\psi$.
4. For $(K, L)$ in Case A and $\ell \ge 5$, the Wach data at $(K, 1, L)$ have a unit generator.
5. The three published inputs give the admitted statements of Theorem E.

With these inputs, a theorem on the local corollary, applied with the constant $10$ for the admitted statements, gives Theorem E with constant $800$ and Corollary A with every constant $C \ge C_0$. $\square$

The bound part of Theorem E does not depend on the local data at all; it is a statement about the numbers $\epsilon$, $\sigma$, $\rho_H$ and $\kappa$.

The arc tools are 13 statements on Wach modules, each asked at every prime and every $(K, L)$ in Case A where it is local. We do not unfold them; we list them by their content:

1. saturation of Wach lattices, in the form used for arc lifting;
2. saturation of Wach lattices, in the étale form;
3. saturation under Frobenius pullback;
4. $\gamma(\pi_0) = \pi_0 u$ for each $\gamma$, with $u$ in the $\Delta$-invariant ring;
5. the killer statement at levels;
6. the killer bound with constant $8$;
7. the killer statement at levels, in a second form;
8. the first filtration statement, for arc lifting;
9. the first filtration statement, in the étale form;
10. the second filtration statement, for arc lifting;
11. the second filtration statement, in the étale form;
12. the filtration properties, in the étale form;
13. a statement that $H^1_f$ is free under base change.

**Theorem 7.18.6 (The arc tools).** For every family of local data, the 13 arc tools hold.

Lean: `GlobalTheory.ArcTools.arc_tools_from_clauses` (also `GlobalTheory.T.arcTheorem_tools_of_wachModuleConclusions`, a second name).

*Proof.* [The clauses on Wach lattices](/entry/wach-lattice-later-clauses-hold/) give ten properties of $\Delta$-invariant lattices, which we call clauses 1 to 10, and seven further clauses; two of these, $(a)$ and $(b)$, are used below. A theorem on Herr complexes, applied to part A of the Herr statement for the local data, gives the naturality of Herr complexes. Each arc tool then follows from a theorem that takes some of these as hypotheses:

1. tools 1 and 2 follow from clauses 1 and 9;
2. tools 3 and 4 follow from clause 9;
3. tool 5 follows from clauses 4 and 9;
4. tool 6 follows from tools 4 and 5;
5. tool 7 follows from tool 4;
6. tools 8 and 9 follow from clauses 2, 5 and 9, clause $(a)$, and the naturality of Herr complexes;
7. tool 10 follows from clauses 7 and 9, clause $(b)$, and tool 8;
8. tool 11 follows from clauses 7 and 9, clause $(b)$, and tool 9;
9. tool 12 follows from clauses 3, 4 and 9;
10. tool 13 holds with no hypothesis.

This gives all 13 tools. $\square$

So clause 9 enters almost every tool, and clauses 6, 8 and 10 and five of the seven further clauses are not used.

**Remark 7.18.7 (Formalization).** The constant $C_0$ is `Formalism.MainNotions.N.Ln03.localCorollaryConstant`, which is `Classical.choose` of an existence theorem ([LocalCorollaryConstant.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/LocalCorollaryConstant.lean#L9)); no value is given. Theorem E with constant $C$ is `WachCoordinates.Conclusion1 D C`, which unfolds to `LiftingTheoremLocalTheory`, the conjunction of `ThmELiftAt` at all data and `ThmEBound C` ([WachCoordinates.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/WachCoordinates.lean#L287)). `ThmEBound` does not mention `D`. Corollary A is `Conclusion2`, that is `LocalCorollaryLifting` and `CorAAt` (line 146). The exponent $\epsilon$ is `ePar`, $\epsilon_0$ is `initialExponentBound`, $\rho_H$ is `rrPar`, $\kappa$ is `kapPar`, and the word condition is `WordOK` (line 24). The five inputs of the first proof are `GlobalTheory.Per.DdREqDcris.record_caseA`, `GlobalTheory.Decompl.fontaine_and_decompletion`, `GlobalTheory.T.fontaine_fullFaithful_exact_psi`, `GlobalTheory.WachUnit.unitGen_exists` and `GlobalTheory.T.localLifting_theoremE_hypotheses_admitted`, and the final step is `Ln03.local_corollary_of_de_rham`, called twice with the same inputs ([TheoremECorollaryAClosingAllData.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremECorollaryAClosingAllData.lean#L30)). In the second proof, the pattern on line 28 of [ArcTheoremToolsOfWachModuleConclusions.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/ArcTheoremToolsOfWachModuleConclusions.lean#L28) names 17 outputs, and `p6`, `p8`, `p10`, `c2`, `c`, `d`, `l3` and `pE` are never used. The arc tools live in the namespace `UnusedSlot80`, but they are used. The étale second filtration theorem is named `FamilyMassExplicitOfVolumeAgreement` ([FiltrationSaturationKiller.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/FiltrationSaturationKiller.lean#L60)), and it has nothing to do with masses or volumes. The conclusion of the clauses theorem is named `DeltaInvariantNormBound`. The second names are one-line wrappers.
