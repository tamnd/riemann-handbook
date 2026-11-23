---
title: Norm-compatible systems of zeta classes
decls:
  - UpperTheory.Kd.K4.top
  - UpperTheory.Kd.K4.kato_eulerSystem_integrality
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Norm-compatible systems of zeta classes

This section takes the zeta classes of the earlier sections, projects them to a two-dimensional [[Galois representation|JQEYEQJY2G]] attached to a newform, and glues them into one norm-compatible family of cocycles $Y_r$ along the cyclotomic $\mathbb{Z}_\ell$-tower, together with one global class $y$. The class $y$ is unramified outside a finite set, it has tame classes at the auxiliary primes, and it is linked to the family $Y_r$ on inertia at $\ell$. These are the properties of an Euler system in the sense of Kato and Rubin. The result is a hypothesis of [the global unit law for smoothed classes](/entry/kato-global-unit-law-of-smoothed-classes/), which with [the Hodge-Tate law for smoothed zeta classes](/entry/smoothed-zeta-class-hodge-tate-law/) proves [the unramified zeta theorem](/entry/zeta-ur/). The background is in [Euler systems and Kato](/learn/galois-cohomology/#euler-systems-and-kato), [Iwasawa theory](/learn/galois-cohomology/#iwasawa-theory) and [Selmer groups](/learn/galois-cohomology/#selmer-and-tate-shafarevich-groups).

### Representations and projections

Fix an odd prime $\ell$, an algebraic closure $\Omega$ of $\mathbb{Q}$ with Galois group $G_{\mathbb{Q}}$, and a field isomorphism $\iota \colon \overline{\mathbb{Q}}_\ell \to \mathbb{C}$. A *coefficient datum* is a subring $\mathcal{O}$ of $\overline{\mathbb{Q}}_\ell$ of integers of a finite extension of $\mathbb{Q}_\ell$.

**Definition 5.4.1.** Let $e \geq 1$, let $S$ be a finite set of places of $\mathbb{Q}$ and let $A$ be a valuation ring of $\Omega$. A representation $W \colon G_{\mathbb{Q}} \to \mathrm{GL}_2(\overline{\mathbb{Q}}_\ell)$ is *a newform-type representation of weight $e$ for $S$ and $A$* if:

1. $W$ is continuous, and its entries lie in some coefficient datum;
2. $S$ contains the places above $\ell$, and $W$ is trivial on the inertia groups at places outside $S$;
3. $(\det W)^2 = 1$, and $\det W(c) = -1$ for each complex conjugation $c$;
4. the restriction of $W$ to a fixed open subgroup is irreducible;
5. $A$ lies over $\ell$; on the decomposition group of $A$, $W$ is upper triangular; on its inertia group, $W_{11}^m = \chi^{em}$ for some $m \geq 1$, where $\chi$ is the cyclotomic character; and $W_{11} \neq \chi$ at some element of the decomposition group.

Let $g$ be a newform of weight $2e+1$ with level $M$ and coefficients $a_q$. We say $g$ is *an unramified source for $W$* if $\ell \nmid M$, $|\iota^{-1}(a_\ell)| = 1$, and there is a character $\chi_0$ of $G_{\mathbb{Q}}$ trivial on the roots of unity of $\ell$-power order such that $g$ is attached through $\iota$ to the twist of $W$ by $\bar\chi^{-e} (\det W)^{-1} \chi_0$, and $W_{22}\, \bar\chi^{e} (\det W)^{-1} \chi_0 = 1$ on the inertia group of $A$. Here $\bar\chi$ is the Teichmüller part of the cyclotomic character.

For a function $\psi$ on $\mathbb{Z}/\ell$, put $\theta(s) = \chi(s)^{-e} \psi(\chi(s) \bmod \ell)$ and $\rho(s) = \theta(s)^{-1} W(s)$.

**Definition 5.4.2.** Let $K$ be a tower, $\mathrm{pr} \colon \mathcal{F} \to \overline{\mathbb{Q}}_\ell^2$, $N \geq 1$, $c_w \colon \mathbb{Z}/N \to \overline{\mathbb{Q}}_\ell$, integers $c, d$, a map $g_m$ and a coefficient datum $\mathcal{O}$. The data are *admissible for $g$* if each $c_w(x)$ lies in $\mathcal{O}$ and, whenever some $c_w(x) \neq 0$:

1. $c, d > 1$ are prime to $6 \ell N$;
2. $\mathrm{pr}$ is additive and $\mathbb{Z}_\ell$-linear, maps $B_{N,\ell}(2e-1)$ into $\mathcal{O}^2$, and satisfies $\mathrm{pr}(s \ast b) = \rho(s)\, \mathrm{pr}(b)$ on $B_{N,\ell}(2e-1)$;
3. on $B_{N,\ell}(2e-1)$, $\mathrm{pr}$ turns the Hecke operator $T_q$ into $\iota^{-1}(a_q)$ and each diamond operator $\langle q \rangle$ into a scalar, for each prime $q \nmid \ell N$;
4. the second row of $g_m(r_0)$ is $u\,(r_0, -1) \bmod \ell$ for a unit $u$, and $N \mid g_m(r_0)_{21}$;
5. there is a character $\chi_0$ as above with $\chi_0(s) = \psi(\chi(s) \bmod \ell)$.

### Zeta systems

**Definition 5.4.3.** A *zeta system for $x \in \mathbb{Z}/N$ with exponent $c_0$* is a family of maps $Y_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$ such that, for all $r$ and $n$, there are a lift $b$ with exponent $c_0$ in weight $2e-1$ of the zeta classes of weight $2e+1$ at level $(r, n)$, and a map $\eta \colon (\mathbb{Z}/\ell^r)^\times \to \mathcal{O}^2$, with
$$Y_r(s, y) \equiv \sum_{y' \mapsto y} \rho(\rho_0(y'))\, \mathrm{pr}\bigl(b_{\rho_0(y')^{-1} s \rho_0(y' \chi(s)^{-1})}\bigr) + \rho(s)\, \eta\bigl(y \chi(s)^{-1}\bigr) - \eta(y) \pmod{\ell^n}.$$
Here $\rho_0$ is the fixed lift of the units mod $\ell^{r+n} N^2$ to $G_{\mathbb{Q}}$ of the [fibre sum](/entry/mackey/), and the sum runs over the units mod $\ell^{r+n}N^2$ above $y$. A *weighted zeta system* is a sum $\sum_x c_w(x) Y_{x,r}$ of zeta systems with one exponent.

### The theorem

**Theorem 5.4.4 (norm-compatible system of zeta classes).** Let $\ell$ be a prime, $e \geq 1$ and $\ell \neq 2$. Let $W$ be a newform-type representation of weight $e$ for $S$ and $A$, and $g$ a newform of weight $2e+1$ that is an unramified source for $W$. Let $K$ be a tower whose modular invariant is holomorphic on $\mathbb{H}$. Let $N \geq 1$ with $\ell \nmid N$. Let $c_w$, not identically zero, $c$, $d$, $g_m$ with each $g_m(r_0) \in \Gamma_1(N)$, $\psi$, $\mathrm{pr}$ and $\mathcal{O}$ be admissible for $g$, and let $W$ be continuous with entries in $\mathcal{O}$. Then there are $c_0, m \in \mathbb{N}$, a coefficient datum $\mathcal{O}'$, a finite set of places $S'$, maps $Y_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell^2$ and a map $y \colon G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$ such that:

1. $(Y_r)$ is a weighted zeta system with exponent $c_0$;
2. $Y_r(st, u) = Y_r(s, u) + \rho(s)\, Y_r(t, u\, \chi(s)^{-1})$;
3. $Y_r(s, u) = \sum_{u' \mapsto u} Y_{r+1}(s, u')$, the sum over the units mod $\ell^{r+1}$ above $u$;
4. each coordinate of $Y_r(s, u)$ is continuous in $s$;
5. for all $r, n$ there is a finite set $E_0 \subset \Omega$ such that $Y_r(ss', u)_2 \equiv Y_r(s, u)_2 \pmod{\ell^n}$ whenever $s'$ fixes $E_0$;
6. the values of $Y_r$ lie in $\mathcal{O}$;
7. $\mathcal{O} \subseteq \mathcal{O}'$;
8. $y(s) \equiv \sum_u \langle u \rangle^{-e} \psi(u \bmod \ell)\, Y_r(s, u) \pmod{\ell^r}$ for each $r$, with $\langle u \rangle$ the least residue of $u$;
9. $\ell^m y$ is a cocycle for $W$ with values in $\mathcal{O}'$; at each place prime to $\ell$ it is a coboundary on some inertia group; and it has tame classes at each prime $w \notin S'$ with $\ell^n \mid w - 1$;
10. the second coordinates of $\ell^m Y_r$ form an Iwasawa system on the decomposition group of $A$ for the character $\rho_{22}$;
11. the second coordinates of $\ell^m Y_r$ and $\ell^m y$ are linked on the inertia group of $A$: for each $n$ and each large $r$, at each $s$ in inertia with $\bar\chi(s) = 1$, $\ell^m y(s)_2$ is congruent mod $\ell^n$ to $\sum_u \langle u \rangle^{-e} \psi(u)\, \ell^m Y_r(s, u)_2$.

Lean: `UpperTheory.Kd.K4.top` (also `UpperTheory.Kd.K4.kato_eulerSystem_integrality`, a second name)

The names point to the Euler system of Kato [Kato 2004]. We do not claim that this exact statement is in that paper. Clauses 2 and 3 are the cocycle law and the norm relation along the tower, as in Rubin's axioms [Rubin 2000].

*Proof.* Fix $x_0$ with $c_w(x_0) \neq 0$.

1. For each $x$ with $c_w(x) \neq 0$ there is $c_1(x)$ such that for each $c_0 \geq c_1(x)$ there is a zeta system $Y_x$ for $x$ with exponent $c_0$ and clauses 2, 3, 4 and 6. Its existence uses [the coefficient law](/entry/law/) only through the lifts; the cocycle law comes from the twisted Galois action, and the norm relation from the push along the fibres. Take $c_0 = \max_x c_1(x)$. The weighted sum keeps clauses 2, 3, 4 and 6, because $c_w$ takes values in $\mathcal{O}$.
2. Write $W = \theta \rho$. The character $\theta$ is continuous, with values in $\mathcal{O}$. It is congruent to $\chi^{-e}$ times the Teichmüller twist on inertia, and the decomposition group acts through upper triangular matrices.
3. A tame relation gives $k$, the set $S'$ and, at each prime $w \notin S'$ with $\ell^n \mid w - 1$, a tame class for $\ell^k Y$. It comes from the action of the Hecke operator $T_w$ through $\mathrm{pr}$.
4. Replace $Y$ by $\ell^k Y$. Clauses 1 to 4 and 6 still hold, with exponent $c_0 + k$.
5. A gluing step along the tower gives $m$, $y$ and clauses 8 to 11. It builds $y$ as a limit of the twisted sums of clause 8, which are compatible by the norm relation.
6. Clause 4 and the compactness of $G_{\mathbb{Q}}$ give the uniform clause 5. Take $\mathcal{O}' = \mathcal{O}$. $\square$

**Remark 5.4.5 (Formalization).** The theorem is in [AdmissibleWeightedDataMonoCoef.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L132), and its second name is at [line 208](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/NormProducts/AdmissibleWeightedDataMonoCoef.lean#L208), the single term `UpperTheory.Kd.K4.top`. That second name is the statement `KatoEulerSystemIwasawaClassStatement` ([SmoothedZetaClassHodgeTateLawStatement.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/FrobeniusHodgeTateLaws/SmoothedZetaClassHodgeTateLawStatement.lean#L11)). It says "integrality", but integrality is one clause of eleven. The predicates are `Nf` ([FinalTheorems.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/FinalTheorems.lean#L53)), `SrcUr`, `AdmWn` and `AdmissibleNewformZetaData` ([AdmissibleNewformZetaData.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/AdmissibleNewformZetaData.lean#L15)), and `IsZWc`. Three things are odd. First, the hypothesis that $g$ is an unramified source is never used (`SrcUr`, line 133). Second, `AdmissibleNewformZetaData` takes $x \in \mathbb{Z}/N$ but never uses it, so `g3` (line 15) gets the condition at every $x$ from the condition at $x_0$ (line 28). Third, the proof takes $\mathcal{O}' = \mathcal{O}$ at line 189, so clause 7 is empty. Clause 4 of our definition of a newform-type representation reads the field `irr` loosely, and we have not unfolded `Coef`, `Tame`, `Layer2` or the gluing lemma `GlobalTheory.KZ.middle_glue2`. Step 1 is `ml` and `shCoc_wsum_props`, step 2 is `GlobalTheory.K4.twist_clauses`, step 3 is `UpperTheory.V.Z.Kato.Nb.kato_tame_relation_projected`, and step 6 is `exists_finset_unif`; our sketches of steps 1, 3 and 5 name what these lemmas give, not how they are proved. In clauses 5, 10 and 11 the Lean index is `1`, the second coordinate. The Iwasawa system of clause 10 is `IwSys2`, the link of clause 11 is `SpLink`, and the character of clause 10 is `nuD`, which is $\rho_{22}$ when it is nonzero and 1 otherwise.
