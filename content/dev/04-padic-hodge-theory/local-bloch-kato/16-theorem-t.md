---
title: Theorem T
decls:
  - GlobalTheory.TheoremTClosing.main
  - GlobalTheory.T.liftingStep_theoremT_of_bhattScholze_fontaine
  - GlobalTheory.InertiaEigenvalues.theoremT_all_records
  - GlobalTheory.T.crystallinePeriodBound_all_constant_ge_forty
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem T

This section proves Theorem T for every constant $C \ge 40$. The statement is about potentially crystalline lattices of $G_{\mathbb{Q}_\ell}$ whose inertia acts through a given set of characters. The proof chooses a tame field over which the lattices become good in the sense of [the section on packs](/entry/exists-pack-is-of-type/), and it then applies [the lifting estimate for good lattices](/entry/lift-f-of-is-good/). A second theorem restates the result from the published inputs of the chapter. The second theorem supplies Theorem T as a local input where the local inputs of the series are collected.

We keep the notation of Section 7 for finite cocycles, coboundaries, and lattice maps that lift with an exponent. Fix a prime $\ell$, a finite extension $K'$ of $\mathbb{Q}_\ell$ such that $G_{K'}$ is a normal subgroup of finite index in $G_{\mathbb{Q}_\ell}$, and assume that $G_{\mathbb{Q}_\ell}$ sends the maximal unramified subfield $K'_0$ of $K'$, inside $B_{\mathrm{cris}}$, to itself. Let $L$ be a finite extension of $\mathbb{Q}_\ell$ with ring of integers $\mathcal{O}$.

**Definition 7.16.1 (Inertia data).** Let $I \subseteq G_{\mathbb{Q}_\ell}$ be the subgroup of elements that fix $K'_0$ in $B_{\mathrm{cris}}$. An element $\mathrm{Fr} \in G_{\mathbb{Q}_\ell}$ is a *Frobenius* if it acts on $K'_0$ as the absolute Frobenius $\sigma$. A finite set $\Sigma$ of characters $I \to L^\times$ is *Frobenius stable* for $\mathrm{Fr}$ if for every $a \in \Sigma$ there is $b \in \Sigma$ with $b(g) = a(\mathrm{Fr}^{-1} g\, \mathrm{Fr})$ for all $g \in I$.

1. A lattice $T$ in a representation $V$ is *potentially crystalline* if $V$ is crystalline on $G_{K'}$.
2. The *inertia of $T$ acts through* $\Sigma$ if every $a \in \Sigma$ is trivial on $I \cap G_{K'}$, the order of every $a \in \Sigma$ is prime to $\ell$, and $D_{\mathrm{cris}}(V|_{G_{K'}})$ is the sum over $a \in \Sigma$ of its $a$-eigenspaces for the action of $I$.
3. The *orbit length* of a character $\chi$ of $I$ is the least $k \ge 1$ with $\chi(h) = \chi(g)$ whenever $h = \mathrm{Fr}^{-k} g\, \mathrm{Fr}^k$. The *period* $r'(\Sigma)$ is the largest, over $\chi_1, \chi_2 \in \Sigma$, of the orbit length of $\chi_1 \chi_2^{-1}$.

**Definition 7.16.2 (Theorem T with constant $C$).** For $C \ge 0$, *Theorem T with constant $C$* for $(K', L)$ is the following statement. Let $g : T_1 \to T_2$ be a map of potentially crystalline $\mathcal{O}$-lattices of $G_{\mathbb{Q}_\ell}$ that is onto. Let $N, \eta, H \ge 0$, let $U \subseteq \mathbb{Z}$ be finite, let $\mathrm{Fr}$ be a Frobenius, and let $\Sigma$ be a Frobenius stable set of characters of $I$ with $1 \in \Sigma$. Assume:

1. $|\Sigma| \le N$ and $N \ge 2$;
2. the inertia of $T_1$ and of $T_2$ acts through $\Sigma$;
3. $-\eta \le u \le H$ for every $u \in U$, $0 \in U$, $|U| \le N + 1$, and $1 \le \eta < H$;
4. at every embedding $\tau$, the Hodge-Tate jumps of $T_1$ and of $T_2$ lie in $U$;
5. $C(HN^2 + N^3) < \ell$.

Then, with $r' = r'(\Sigma)$, we have $4 r' \le N^2$, and $g$ lifts with exponent $C(N r' + \eta(N + r'))$.

*Theorem T with constant $C$* for a family of local theories is this statement at every prime $\ell$, for every such $K'$ and every $L$.

**Theorem 7.16.3 (Theorem T).** Assume the theorem of Bhatt and Scholze on crystalline lattices and the theorem of Fontaine. Let $C \ge 40$. Then for every family of local data, Theorem T with constant $C$ holds.

Lean: `GlobalTheory.TheoremTClosing.main` (also `GlobalTheory.T.liftingStep_theoremT_of_bhattScholze_fontaine`, a second name).

*Proof.* Fix $\ell$, $K'$ and $L$, and the data of the statement.

*Step 1: the tame level.* Put $a = (\ell - 1)!$ and $e = \ell^a - 1$. Then $a \ge 1$, $e \ge 1$, and $\ell \nmid a$, since every factor of $(\ell - 1)!$ is less than $\ell$.

*Step 2: a larger field of coefficients.* Since $e + 1 = \ell^a$ and $\ell \nmid a$, a lemma on coefficient fields gives a finite extension $L' \supseteq L$ that contains the unramified field of degree $a$ and has tame descent data. A descent lemma says that Theorem T with constant $C$ for $(K', L')$ implies it for $(K', L)$. So we may replace $L$ by $L'$.

*Step 3: the numbers.* Choose any system of roots $\varpi$, and take the standard period data of the local theory. From $C \ge 40$ and hypothesis 5 we get $40(HN^2 + N^3) < \ell$, and from $N \le N^3$ we get $N < \ell$. By hypothesis 2 every character in $\Sigma$ is trivial on $I \cap G_{K'}$ and has order prime to $\ell$.

*Step 4: the tame type.* By [the theorem on the tame field](/entry/exists-tame-field-good-lattice-potentially-crystalline/), which uses the theorem of Fontaine, there is a set $\Sigma' \subseteq \mathbb{Z}/e$ with $\ell c \in \Sigma'$ for $c \in \Sigma'$, $0 \in \Sigma'$, $|\Sigma'| \le N$ and $r(\Sigma') = r'(\Sigma)$. Also, every potentially crystalline lattice whose inertia acts through $\Sigma$ is crystalline over $K_\varpi$ and has tame type $\Sigma'$. With hypothesis 4, $T_1$ and $T_2$ are good for $(\Sigma', U)$.

*Step 5: the lifting estimate.* The numerical conditions of Section 15 hold for $(\ell, e, N, \eta, H, \Sigma', U)$: the conditions on $\Sigma'$ come from Step 4, those on $U$, $N$ and $\eta$ are hypotheses, and $40(HN^2 + N^3) < \ell$ comes from Step 3. By [the lifting estimate](/entry/lift-f-of-is-good/), $g$ lifts with exponent $7(N r' + \eta(N + r'))$.

*Step 6: the period bound.* A lemma on periods in $\mathbb{Z}/e$ says that under the conditions on $\Sigma'$ of Step 4 and $N \ge 2$, we have $1 \le r(\Sigma')$, $4 r(\Sigma') \le N^2$, and every $c \in \Sigma'$ has period at most $r(\Sigma')$. So $4 r' \le N^2$.

*Step 7: a larger exponent.* If $g$ lifts with exponent $s$ and $s \le s'$, then $g$ lifts with exponent $s'$: for $z \in Z^1_f(T_2)$, $\ell^{s'} z = \ell^{s' - s}(\ell^s z)$, and $g_* Z^1_f(T_1) + B^1(T_2)$ is a submodule. Since $7 \le 40 \le C$, $7(N r' + \eta(N + r')) \le C(N r' + \eta(N + r'))$. So $g$ lifts with exponent $C(N r' + \eta(N + r'))$. $\square$

The second theorem states Theorem T from the published inputs. The integral form of the theorem of Bhatt and Scholze, [Theorem 6.13.4](/entry/bhatt-scholze-integral/), is about $\mathbb{Z}_\ell$-lattices. We do not unfold it.

**Theorem 7.16.4 (Theorem T from the published inputs).** Assume the integral theorem of Bhatt and Scholze, the theorem of Fontaine, the Bloch-Kato dimension formula, local Tate duality and the local Euler characteristic formula. Let $C \ge 40$. Then for every family of local data, with Hodge-Tate, Fontaine and comparison data, Theorem T with constant $C$ holds.

Lean: `GlobalTheory.InertiaEigenvalues.theoremT_all_records` (also `GlobalTheory.T.crystallinePeriodBound_all_constant_ge_forty`, a second name).

*Proof.* A lemma on coefficients shows that the integral theorem of Bhatt and Scholze implies the theorem on crystalline lattices with coefficients in $\mathcal{O}$. The Bloch-Kato formula, local Tate duality and the Euler characteristic formula give a list of admitted local statements for the local data. Then [Theorem T](/entry/theorem-tclosing-main/) applies. $\square$

The admitted local statements of this proof are not used: the first theorem holds without them. So the Bloch-Kato formula, local Tate duality, the Euler characteristic formula and the comparison data are not needed for Theorem T.

**Remark 7.16.5 (Formalization).** In Lean, Theorem T with constant $C$ is `thmT`, and the family version is `Conclusion2 D C`, which unfolds to `CorollaryALocal D.loc C` ([ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L201)). So the name says Corollary A, but the content is Theorem T. The statement of `main` is `HodgeTateFromSandwich D HW F C`, which is `Adm2 D HW F → Conclusion2 D C` (line 224). The proof introduces the hypothesis `Adm2` as `_` and never uses it ([LiftingStepTheoremTOfBhattScholzeFontaine.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingStepTheoremTOfBhattScholzeFontaine.lean#L39)). As a result, the hypotheses `BlochKatoLocal`, `LocalTateDualityK`, `LocalEulerCharK` and `Cm` of `theoremT_all_records` only feed this unused argument ([CrystallinePeriodBoundAllConstantGeForty.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallinePeriodBoundAllConstantGeForty.lean#L19)). The coefficient lemma `exists_coeffField_containsUnramifiedWitt_tameDescent` is called twice, once for $L$ (its second part is discarded, line 53) and once for $L'$ (line 55). The system of roots is `Classical.arbitrary _` (line 57). Step 7 is the local lemma `liftF_of_le` (line 28). The steps use the lemmas `theoremT_descend_smaller_coefficients`, `exists_tameField_goodLattice_potentiallyCrystalline`, `maxFrobeniusOrbitLengthDiff_bounds_zmod` and `bhattScholze_coefficients_of_padicInt_lattices`, which we read only through their statements. The second names are one-line wrappers.
