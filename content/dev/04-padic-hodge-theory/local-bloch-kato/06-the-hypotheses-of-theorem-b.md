---
title: The hypotheses of Theorem B
decls:
  - GlobalTheory.T.localLifting_theoremB_hypotheses_admitted
  - GlobalTheory.TheoremBAdm.admissible_ranks_of_CMDatum
  - GlobalTheory.T.crystallineUniversalPart_caseA
  - GlobalTheory.universalPart_caseA
  - GlobalTheory.T.classSplitting_along_arcs_of_admissible
  - GlobalTheory.classSplitAlongArcs
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The hypotheses of Theorem B

Theorem B of the next section bounds congruence lengths of maps of crystalline lattices. Its proof takes 13 statements on Wach modules and Galois cohomology as hypotheses. This section proves that the 13 statements hold for the local data of the series, with the constants $(C_R, C_A, C_B, C_K, C_\kappa) = (10, 23, 32, 32, 8)$. Two of them, the splitting of classes along arcs and the universal part, are proved here from other statements on Wach modules. The result is used in [Theorem B](/entry/theorem-b-closing/).

We keep the notation of Sections 1 and 3. Let $D$ be the data of the series and $H$, $F$, $C$ local data over $D$, as in Section 5. At a prime $\ell$ and fields $(K, L)$ in Case A the Wach data of $H_\ell$ give letters $i \in \mathbb{Z}/n$, a Wach module $D(T)$ for each lattice $T$ with its $\Delta$-invariant parts, the operators $\varphi$ and $\gamma$, and the element $\pi_0$ of the ring of the letters.

**Definition 7.6.1 (Arc datum).** An *arc datum* for $n$ consists of integers $G_0, S, \eta, h, j \ge 0$, a type $\mathrm{ty}(i)$ for each letter $i$ (thin, or thick of kind up or down with a size), a finite set of *cuts* in $\mathbb{Z}/n$, and a length $\mathrm{len}(c)$ for each cut. It is *good* if these conditions hold:

1. there is a cut, and $j \ge 1$;
2. for each cut $c$: $j \le \mathrm{len}(c) \le n$, $c - \mathrm{len}(c)$ is a cut, and $c - d$ is not a cut for $1 \le d < \mathrm{len}(c)$;
3. each type is admissible for $\eta$, $G_0 \le h$, $1 \le h$, and every thick type has size at most $h - S$;
4. either the $j$ letters after each cut are thin, or $j = 1$, all types are thick, and the letter after each cut has size at most $G_0 - S$.

Put $M(\ell) = \lfloor 2h/(\ell - 1) \rfloor + 1$ and $\sigma(\ell) = \lceil (2G_0 + M(\ell)/\ell^{j-1})\,\ell/(\ell-1)^2 + 1 \rceil$. A lattice $T$ is *in the window* of the arc datum if $T$ is crystalline and, at each letter $i$, its jumps at the embeddings over $\tau_i$ lie in a window fixed by $\mathrm{ty}(i)$, $G_0$, $S$ and $\eta$. We do not unfold the admissibility of a type or the window.

**Definition 7.6.2 (Splitting statement).** The *splitting statement* at $(K, L)$ is: let $\ell \ge 5$ and let $A$ be a good arc datum. Let $T_2$ and $Y$ be lattices, $\iota : T_2 \to Y$ and $\pi : Y \to \mathcal{O}$ maps, with $T_2$ in the window of $A$ and $Y$ crystalline, and let $z$ be a cocycle of $T_2$ such that $Y$ is the extension of $\mathcal{O}$ by $T_2$ given by $z$: the sequence is exact and there is $e \in Y$ with $\pi(e)$ a generator and $\iota(z(g)) = g e - e$. Let $r \ge 0$ be such that, at each cut, $\ell^r$ times each $\Delta$-invariant element of the Wach module of $\mathcal{O}$ lies in the image of the Wach module of $Y$. Then there are elements $w_c \in D(T_2)$ and classes $x_c \in H^1(K, T_2)$, for the cuts $c$, such that
$$\ell^{\,r + 2\sigma(\ell)} [z] = \pm \sum_{c} x_c,$$
where each $w_c$ satisfies integrality and filtration conditions at $c$ and $x_c$ is the class that $w_c$ defines at $c$. We do not unfold these conditions.

**Definition 7.6.3 (Universal statement).** The *universal statement* at $(K, L)$ has two parts, for $\ell \ge 5$ and good arc data. The first says how an element of the inertia module at a cut is a combination of a horizontal basis with integral coefficients. The second says: if $T_2$ is in the window and has at most $m$ low jumps at each thick letter, then at each cut $c$ there is a horizontal basis with at most $m \cdot \rho(c)$ exceptional elements, and the invariants are generated, modulo $\pi_0$, by at most $m \cdot \rho(c) \cdot (\mathrm{len}(c) + 1)$ elements, where $\rho(c)$ is a count of letters fixed by the types. We do not unfold the rest of the statement.

**Definition 7.6.4 (Admitted statements of Theorem B).** For constants $(C_R, C_A, C_B, C_K, C_\kappa)$, the *admitted statements of Theorem B* are 13 statements, each asked for all primes $\ell$ and all $(K, L)$ in Case A with $\ell \ge 5$ when it is local:

1. the used local conclusion on $\Delta$-invariant lattices;
2. eight local lifting statements on Wach modules with the constants $C_R$, $C_A$, $C_B$, $C_K$;
3. saturation of Wach lattices;
4. saturation under Frobenius pullback;
5. five killer statements: two on window sums, one on levels, one modulo $\ell$, and the inequality $\kappa(C_\kappa)$ below;
6. the divisibility statement below;
7. a bound on the number of generators of $H^1_f$;
8. the relay statement;
9. the arc coordinates;
10. the splitting statement;
11. the universal statement;
12. strict exactness of $D_{\mathrm{cris}}$ on sequences of crystalline representations;
13. the Bloch-Kato extension criterion.

We do not unfold statements 1 to 4, 7 to 9 and the first four parts of 5. The inequality $\kappa(C)$ says: for a prime $\ell \ge 5$, integers $G \le h$ with $1 \le h$, $S, t, \rho \ge 0$, and integers $a_1, \dots, a_\rho$ with $-2h \le a_k$ and $a_k + S \le 2h$, put $J = [-2G, G] \cup \bigcup_k [a_k, a_k + S)$; then
$$t + \sum_{x \in J,\, x \ne 0} \big(t + 1 + v_\ell(x)\big) \le C\big((G + \rho S + 1)(t+1) + (\rho + 1)\log_\ell h\big).$$
The divisibility statement says: let $\mathcal{O}$ be a discrete valuation ring with uniformizer $\varpi$, $\ell = u\varpi^e$ with $u$ a unit and $e \ge 1$, $f \in \mathcal{O}[[X]]$ with $v_\varpi(f(0)) = e v$ exactly, and $a, A', y, B, k \ge 0$ with $y + A' + a + v + 1 \le B$. If $\ell^a f (X - \ell)^{A'} X^y$ lies in the ideal $(\varpi^k, X^B)$, then $k/e < a + v + 1$.

**Theorem 7.6.5 (Class splitting along arcs).** Assume, for the local data, the hypotheses of the splitting (two properties of $\Delta$-invariant lattices, the annihilators, the jump statement, the formula for Herr extension classes, the first filtration, the relay statement and the arc coordinates), the hypotheses of the arc coordinates, freeness of Wach lattices, a further property of $\Delta$-invariant lattices, that Wach modules kill quotients, the Fontaine equivalence with $\psi$, and two exactness statements for $D_{\mathrm{cris}}$. Then the splitting statement holds at every $(K, L)$ in Case A.

Lean: `GlobalTheory.T.classSplitting_along_arcs_of_admissible` (also `GlobalTheory.classSplitAlongArcs`).

*Proof.* Freeness, the hypotheses of the arc coordinates and the exactness of $D_{\mathrm{cris}}$ give a bound on local lengths: at every cut the relevant element lies in the critical set. With the arc coordinates this gives the condition at level zero. The splitting in Case A, applied to the hypotheses and this condition, gives the statement. $\square$

**Theorem 7.6.6 (Universal part in Case A).** Assume saturation of Wach lattices, the killer statement on levels, that $\gamma(\pi_0) = \pi_0 u$ for each $\gamma$ with $u$ in the $\Delta$-invariant ring, the arc coordinates, a property of $\Delta$-invariant lattices, a statement on Herr classes, and $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ for unramified $K$. Then the universal statement holds at every $(K, L)$ in Case A.

Lean: `GlobalTheory.T.crystallineUniversalPart_caseA` (also `GlobalTheory.universalPart_caseA`).

*Proof.* The property of $\Delta$-invariant lattices gives a ring condition on the polynomial of the uniformizer, and from it the algebraic tools at each $(K, L)$ in Case A. These tools give the inverse levels at every cut. The universal statement follows from the inverse levels and the hypotheses. $\square$

**Theorem 7.6.7 (Hypotheses of Theorem B).** Assume the theorem of Bloch and Kato, local Tate duality and the local Euler characteristic formula. Then the admitted statements of Theorem B hold for the local data with the constants $(10, 23, 32, 32, 8)$.

Lean: `GlobalTheory.T.localLifting_theoremB_hypotheses_admitted` (also `GlobalTheory.TheoremBAdm.admissible_ranks_of_CMDatum`).

*Proof.* [The clauses on Wach lattices](/entry/wach-lattice-later-clauses-hold/) give freeness and three properties of $\Delta$-invariant lattices. [The local lifting statements with fixed constants](/entry/local-constants-from-admitted-local-galois-statements-alt/) give statement 2 and, from its parts, the annihilators and the Herr classes. The theorem on arc tools gives saturation (statement 3), saturation under pullback (statement 4), the condition on $\gamma(\pi_0)$, the killer statements (statement 5) and the first filtration. The relay theorem gives the relay statement (statement 8) and the hypotheses of the arc coordinates, and with freeness and exactness of $D_{\mathrm{cris}}$ these give the arc coordinates (statement 9). The jump statement comes from the tie, the formula for Herr extension classes holds for the local data, and strict exactness of $D_{\mathrm{cris}}$ holds (statement 12). [Class splitting along arcs](/entry/class-splitting-along-arcs-of-admissible/) gives statement 10, and [the universal part](/entry/crystalline-universal-part-case-a/), with $D_{\mathrm{dR}} = D_{\mathrm{cris}}$ for unramified $K$, gives statement 11. Statement 1 is a used form of the local conclusions on Wach modules, statement 6 is proved directly, statement 7 is the bound on generators of $H^1_f$, and statement 13 is the extension criterion of the tie. $\square$

**Remark 7.6.8 (Formalization).** The three published inputs go only to the local lifting theorem and to the relay theorem, and the local lifting theorem ignores them ([LocalConstantsFromAdmittedLocalGaloisStatements.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/LocalConstantsFromAdmittedLocalGaloisStatements.lean#L14) is `fun _ _ _ D HW F Cm => ...`). So the theorem holds without them. The divisibility statement does not depend on $D$, although it is written as a statement about $D$. The list of 13 statements skips four statements of the same file that have numbers 3, 4, 6 and 7. The main Lean name speaks of ranks and CM data; the statement has neither, and a second theorem with the same short name proves the hypotheses of Theorem C.
