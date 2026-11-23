---
id: theorem-tclosing-main
title: Theorem T at each prime, from Bhatt-Scholze and Fontaine
kind: theorem
decl: GlobalTheory.TheoremTClosing.main
module: Development.AbelianVarietyTheory.Proofs.InertiaEigenvalues.LiftingStepTheoremTOfBhattScholzeFontaine
covers: 2988
status: drafted
drafted_by: writer@claude
---
This theorem proves the local lifting statement `thmT` ("Theorem T" in the Lean names) at every prime $\ell$, for every constant $C \ge 40$, from two published inputs. The wrapper [`liftingStep_theoremT_of_bhattScholze_fontaine`](/entry/lifting-step-theorem-t-of-bhatt-scholze-fontaine/) restates it. [`theoremT_all_records`](/entry/theorem-t-all-records/) uses it to get `Conclusion2` for each datum, and that result goes to [the closing local inputs](/entry/closing-local-inputs-main-alt-alt/) of branch 1 of [the unitary hypotheses node](/proof/unitary-hypotheses/).

## Statement

Fix a prime $\ell$ and let $G = G_{\mathbb{Q}_\ell}$. Let $L/\mathbb{Q}_\ell$ be a finite extension. A *lattice* (`LocLat`) is a finite-dimensional continuous representation $V$ of $G$ over $L$ with a $G$-stable free $\mathcal{O}_L$-lattice $T \subset V$ that spans $V$. The period rings are an abstract package `LocPrime` with rings $B$ and $B_{\mathrm{dR}}$ in the roles of $B_{\mathrm{cris}}$ and $B_{\mathrm{dR}}$ ([period rings](/learn/galois-representations/#period-rings)).

Let $Z^1_f(T)$ be the set of continuous cocycles $c \colon G \to T$ such that $c(g) \otimes 1 = gx - x$ for some $x \in V \otimes B$, and let $B^1(T) = \{g \mapsto gx - x : x \in T\}$. So $Z^1_f(T)/B^1(T)$ is a lattice form of the Bloch-Kato group $H^1_f$ ([Selmer groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups)). A $G$-map $g \colon V_1 \to V_2$ with $g(T_1) \subset T_2$ *lifts with exponent* $e$ (`LiftF`) if $\ell^e Z^1_f(T_2) \subset g_* Z^1_f(T_1) + B^1(T_2)$. Equivalently, $\ell^e$ kills the cokernel of $Z^1_f(T_1)/B^1(T_1) \to Z^1_f(T_2)/B^1(T_2)$.

**Theorem.** Assume `BhattScholzeCrystallineLattices` and `FontaineBcris`. Let $C \ge 40$ and let $D$ be a datum (`D7`). Then `HodgeTateFromSandwich D HW F C` holds. Its conclusion is the following, for each $\ell$, each finite $K'/\mathbb{Q}_\ell$ with $G_{K'}$ normal of finite index in $G$ (and its maximal unramified subfield $K'_0$ stable), and each $L$, with the period rings of $D$ at $\ell$. Let $I \subset G$ be the subgroup that fixes $K'_0$. Let $g \colon T_1 \to T_2$ be a map of lattices onto $T_2$, let $N, \eta, H \ge 0$, let $U \subset \mathbb{Z}$ be finite, let $\Sigma$ be a finite set of characters $I \to L^\times$ and let $\mathrm{Fr} \in G$. Suppose:

1. $V_1$ and $V_2$ are crystalline over $K'$;
2. $\mathrm{Fr}$ acts on $K'_0$ as Frobenius, $\Sigma$ is stable under conjugation by $\mathrm{Fr}$, $1 \in \Sigma$, $|\Sigma| \le N$ and $N \ge 2$;
3. each $\chi \in \Sigma$ is trivial on $I \cap G_{K'}$ and has order prime to $\ell$, and $D_{\mathrm{pcris}}(V_i)$ is the sum of the $\chi$-eigenspaces of $I$ for $\chi \in \Sigma$;
4. $U \subset [-\eta, H]$, $0 \in U$, $|U| \le N + 1$, $1 \le \eta < H$, and the Hodge-Tate jumps of $V_1$ and $V_2$ at each embedding lie in $U$;
5. $C(HN^2 + N^3) < \ell$.

Let $r$ be the largest, over $\chi, \chi' \in \Sigma$, of the least $k \ge 1$ such that $\chi\chi'^{-1}$ is invariant under conjugation by $\mathrm{Fr}^k$. Then $4r \le N^2$, and $g$ lifts with exponent $C(Nr + \eta(N + r))$.

`BhattScholzeCrystallineLattices` says: for each finite $K/\mathbb{Q}_\ell$, each crystalline lattice of $G_K$ is the realisation over $W(\mathcal{O}_{C^\flat})$ of a prismatic F-crystal on $\mathcal{O}_K$, and each $G_K$-map of the lattices lifts to a unique map of F-crystals. Its name points to the theorem of Bhatt and Scholze (2023) in [prismatic Dieudonné theory](/learn/formal-groups/). `FontaineBcris` is a list of seven properties of a crystalline period ring `Core`, among them a fundamental exact sequence and the surjectivity of $\varphi - 1$. We did not unfold `Core`.

## Proof

1. Put $a = (\ell - 1)!$ and $e = \ell^a - 1$. Then $\ell \nmid a$. `exists_coeffField_containsUnramifiedWitt_tameDescent` gives $L' \supset L$ that contains the unramified extension of degree $a$ and a primitive $e$-th root of unity. `theoremT_descend_smaller_coefficients` proves the statement for $L$ from the statement for $L'$. So we may replace $L$ by $L'$.
2. Choose a system $\varpi$ of roots with $\varpi_0^e = -\ell$ and $\varpi_{n+1}^\ell = \varpi_n$. The tame field is the unramified extension of degree $a$ with $\varpi_0$ adjoined.
3. `exists_tameField_goodLattice_potentiallyCrystalline` (from `FontaineBcris`) replaces $\Sigma$ by a set $\Sigma' \subset \mathbb{Z}/e$. It is stable under $x \mapsto \ell x$, contains $0$, has at most $N$ elements, and its largest Frobenius period of differences is $r$. Each $T_i$ is crystalline over the tame field, with tame type $\Sigma'$. With hypothesis 4, $T_1$ and $T_2$ are good in the sense of [the lifting theorem](/entry/lift-f-of-is-good/).
4. Hypotheses 2, 4 and 5 give the numerical conditions `Numerics`, with $40(HN^2 + N^3) < \ell$ because $C \ge 40$.
5. [`lift_surjection_good_crystalline_lattices`](/entry/lift-surjection-good-crystalline-lattices/) gives that $g$ lifts with exponent $7(Nr + \eta(N + r))$.
6. `maxFrobeniusOrbitLengthDiff_bounds_zmod` gives $4r \le N^2$.
7. `liftF_of_le` (in the same file): lifting with exponent $e$ implies lifting with each $e' \ge e$. Use $7 \le C$.

## In the Lean code

The theorem is in [LiftingStepTheoremTOfBhattScholzeFontaine.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LiftingStepTheoremTOfBhattScholzeFontaine.lean#L37). `thmT`, `Conclusion2` and `HodgeTateFromSandwich` are in [ElementDenominator.lean](lean:Formalism/SharpRestriction/LevelLetterCocycles/ElementDenominator.lean#L178), and `LiftF` in [Statement.lean](lean:Formalism/WeaklyAdmissibleFiltrations/Statement.lean#L265). We did not open the proofs of the lemmas that the proof calls.

Odd points:

- `HodgeTateFromSandwich D HW F C` is the implication `Adm2 D HW F → Conclusion2 D C`. The proof never uses `Adm2`: it is the `_` in the `intro` at line 39. $HW$ and $F$ are not used either. So `theoremT_all_records` builds `Adm2` from `BlochKatoLocal`, `LocalTateDualityK` and `LocalEulerCharK` ([line 19](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/CrystallinePeriodBoundAllConstantGeForty.lean#L19)) for no purpose.
- The proof gives the exponent with the constant 7. $C$ enters only through the condition $C(HN^2 + N^3) < \ell$.
- The name `HodgeTateFromSandwich` does not describe the conclusion, which is a lifting statement on crystalline cocycles.
- The base field is $\mathbb{Q}_\ell$ only: `qlExt ℓ` is the bottom intermediate field.
