---
title: A length bound for the cotangent lattice
decls:
  - UpperTheory.V.Alg.M.core_holds
  - UpperTheory.V.Alg.M.main_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A length bound for the cotangent lattice

This section proves the main theorem of the algebra of Section 6.11. A weighted algebra $A$ with a smooth fixed point $x$ is cut by equations $I$. The theorem bounds the cotangent length of the weight $-1$ equations by twice the sum of the valuations $v(\xi(a))$ of one function $a$ of weight $0$ over a set of representatives $\xi$ of the orbits of two-signed points of $\operatorname{Spec} A/I$. In the Galois row, $A$ is a deformation ring with a grading of the kind given in Section 6.13. The theorem is used by [Theorem 7.7.4 of Volume 9](/entry/abstract-count/) and by [Theorem](/entry/vwin-of-hypotheses-h-e-alt/), on the way to [VWin](/step/vwin-def/). The proof has two parts. The core bound, [Theorem 6.12.7](/entry/core-holds/), works in a chart without weight zero and with the weight $-1$ equations in a normal form. It compares the lower bound [Theorem 6.11.8](/entry/low-holds/) of Section 6.11 with an upper bound for the same multiplicity symbol. The main theorem, [Theorem 6.12.8](/entry/main-holds/), puts the data in that form.

### Points, orbits and the conditions

We keep the notation of Section 6.11: $\mathcal{O}$ is a complete discrete valuation ring of characteristic $0$ with fraction field $L$, $A$ is a weighted algebra with fixed point $x$, and $I$ is the ideal of a system of equations $(F, G, E, E', Z)$ with counts $(r, s, r', s', m)$. Let $K$ be an [[algebraically closed|0PF6TM8TWT]] field with an injective map $\mathcal{O} \to K$.

**Definition 6.12.1 (Points and orbits).** A *point* is an $\mathcal{O}$-algebra map $\xi : A \to K$. It lies *on $S$* if $\xi(I) = 0$. It is *negative-zero* if $\xi(A_j) = 0$ for all $j < 0$, *positive-zero* if $\xi(A_j) = 0$ for all $j > 0$, and *two-signed* if it is neither. For $t \in K^\times$ the point $t \cdot \xi$ is $f \mapsto t^j \xi(f)$ for $f \in A_j$. Two points are in the *same orbit* if one is $t \cdot$ the other for some $t$.

Lean: `UpperTheory.V.Alg.OnS`, `UpperTheory.V.Alg.NegZero`, `UpperTheory.V.Alg.PosZero`, `UpperTheory.V.Alg.TwoSigned`, `UpperTheory.V.Alg.act`, `UpperTheory.V.Alg.SameOrbit`.

A point is negative-zero and positive-zero exactly when it factors through $A \to A_0$. Two points with the same restriction to $A_0$ and with both signs present need not be in the same orbit, but the torus moves each two-signed point along a curve with the same restriction to $A_0$.

**Definition 6.12.2 (Covering set).** A finite set $T$ of points *covers* $S$ if each element of $T$ is a two-signed point on $S$, and each two-signed point on $S$ is in the orbit of some element of $T$.

Lean: `UpperTheory.V.Alg.Covers`.

**Definition 6.12.3 (Valuation on $K$).** A *valuation normalized on $\mathcal{O}$* is a function $v : K \to \mathbb{R}$ such that $v(yz) = v(y) + v(z)$ and $\min(v(y), v(z)) \le v(y + z)$ for nonzero $y$, $z$ and $y + z$, and $v(c) = \operatorname{ord}_\varpi(c)$ for nonzero $c \in \mathcal{O}$.

Lean: `UpperTheory.V.Alg.IsNVal`.

For a two-signed point $\xi$ on $S$, a *point derivation* at $\xi$ is an $\mathcal{O}$-linear map $D : A \to K$ with $D(fg) = \xi(f) D(g) + \xi(g) D(f)$.

**Definition 6.12.4 (The conditions).** For the system of equations and an element $a \in A$ we consider:

- (M1) $r \ge 1$; the point $x$ is smooth with $r$, $s$, $r' + 1$, $s' + 1$ and $m$ variables of weights $-1$, $-2$, $1$, $2$ and $0$; the families $F$, $G$ and $Z$ span $C_{-1}$, $C_{-2}$ and $C_0$ up to scalars.
- (M2) The image of $A_0$ in $A/I$ is a finitely generated $\mathcal{O}$-module.
- (M3) Let $x_1 \ne x$ be a point on $S$ that factors through $A_0$. Then either no negative-zero point on $S$ that is not positive-zero, or no positive-zero point on $S$ that is not negative-zero, has the same restriction to $A_0$ as $x_1$.
- (M4) At each two-signed point $\xi$ on $S$, any two point derivations that vanish on $I$ are linearly dependent over $K$.
- (M5) $a \in A_0$, $x(a) = 0$, and $\xi(a) \ne 0$ for each two-signed point $\xi$ on $S$.

Lean: `UpperTheory.V.Alg.M1`, `UpperTheory.V.Alg.M2`, `UpperTheory.V.Alg.M3`, `UpperTheory.V.Alg.M4`, `UpperTheory.V.Alg.M5`, `UpperTheory.V.Alg.mDims`, `UpperTheory.V.Alg.PtDer`.

Condition M2 says that $\operatorname{Spec} (A/I)_0$ is finite over $\mathcal{O}$, so the two-signed points on $S$ fall into finitely many orbits. Condition M4 says that the orbit of a two-signed point is a reduced curve in $S \otimes K$: its tangent space has dimension at most one. Condition M3 says that over a point of $\operatorname{Spec} A_0$ other than $x$, the fibre of $S$ does not contain both an attracting and a repelling half-line of the torus action. In M1 the weight $1$ and weight $2$ counts are one more than the numbers $r'$ and $s'$ of equations of these weights.

### Two lemmas on the Rees algebra

Let $R$ be the Rees algebra of Section 6.11 and $\mathbf{t}$ its list of equations. For an element $b \in A_0$ we write $(0, b)$ for $b$ placed in degree $0$ of $R$.

**Lemma 6.12.5 (Admissibility).** Assume that $F$ and $G$ span $C_{-1}$ and $C_{-2}$ up to scalars, and M2, M3 and M5 for $a$. Let $J \subseteq R$ be an ideal that contains $Z_1, \dots, Z_m$. Then the list $\mathbf{t}$ followed by $(0, a)$ is admitted for $J$.

Lean: `UpperTheory.V.Alg.M.admissibility_holds`.

*Proof.* The ideal $\mathfrak{m}_{A_0} R \cdot R_{e_0} R_{e_1} R_{e_2}$ is finitely generated, so it is enough to show that it lies in the radical of $J' = J + (\mathbf{t}) + aR$, that is, in every prime $\mathfrak{p} \supseteq J'$. If $\mathfrak{p}$ contains $R_{e_0} R_{e_1} R_{e_2}$, this is clear. Otherwise, the contraction $\mathfrak{p} \cap A_0$ contains $I \cap A_0$ up to radical. By M2 it is the maximal ideal of $A_0$, which gives the claim, or it is the kernel of a map $\sigma : A_0 \to K$ that kills $I \cap A_0$. In the second case, if $\sigma(fg) \ne 0$ for some $f \in A_{-2}$ and $g \in A_2$, then $\sigma$ extends to a point $\xi$ on $S$ that is two-signed, and $\xi(a) = \sigma(a) = 0$ contradicts M5. So $\sigma$ kills $A_{-2} A_2$. Then the spanning conditions on $F$ and $G$, together with M3 for the restriction of $\sigma$, show that $\mathfrak{p}$ contains $R_{e_0} R_{e_1} R_{e_2}$, which was excluded. $\square$

**Lemma 6.12.6 (Upper bound).** Assume the hypotheses of the previous Lemma, M4, and let $T$ cover $S$ and $v$ be a valuation normalized on $\mathcal{O}$. Let $J \subseteq R$ be a homogeneous ideal that contains $Z_1, \dots, Z_m$ and the elements of $\mathbf{t}$. Then for large $\mu \in \mathbb{Z}^3$,
$$\chi\bigl(((0, a)), R/J\bigr)(\mu) \le 2^{r + 1 + r'} \sum_{\xi \in T} v(\xi(a)).$$

Lean: `UpperTheory.V.Alg.M.up_holds`.

*Proof.* Put $M = (R/J)_\mu$, a finitely generated $A_0$-module. The left side is $\operatorname{length}(M/aM) - \operatorname{length}(0 :_M a)$. For large $\mu$, the module $M$ is killed by an ideal of $A_0$ whose points over $K$ are restrictions to $A_0$ of two-signed points on $S$, by the argument of the previous Lemma. For such a module, the difference of lengths is at most $\sum_\sigma \ell_\sigma(M) \, v(\sigma(a))$, a sum over the maps $\sigma : A_0 \to K$ in the support, where $\ell_\sigma(M)$ is the length of $M$ at $\sigma$ and $v(\sigma(a)) \ge 0$ by M2. Each such $\sigma$ is the restriction of an element of $T$, since $T$ meets each orbit and the torus does not change the restriction to $A_0$. By M4, the weight pieces of $A/I$ at a two-signed point have local length at most $1$, and this gives $\ell_\sigma(M) \le 2^{r + 1 + r'}$. $\square$

### The core bound

**Theorem 6.12.7 (Core bound).** Let $v$ be a valuation normalized on $\mathcal{O}$. Let $A$ be a weighted algebra, with a system of equations with counts $(r, s, r', s', m)$ and $r \ge 1$. Let $\varphi : A \to L[[\tau]]$ be a chart without weight zero with $r$, $s$, $r' + 1$ and $s' + 1$ variables of weights $-1$, $-2$, $1$ and $2$, with $\varphi(Z_i) = 0$ for all $i$. Let $y_0, \dots, y_{r-1} \in A_{-1}$ and $c_0, \dots, c_{r-1} \in \mathbb{N}$ with $F_i - \varpi^{c_i} y_i \in \mathfrak{s}$ for $i < r$, and assume $F_r \in \mathfrak{s}$. Assume that $F$ and $G$ span $C_{-1}$ and $C_{-2}$ up to scalars, and M2, M3 and M4. Let $a$ satisfy M5 with $\varphi(a) \ne 0$, and let $T$ cover $S$. Then
$$\sum_{i < r} c_i \le 2 \sum_{\xi \in T} v(\xi(a)).$$

Lean: `UpperTheory.V.Alg.M.core_holds`.

*Proof.* Let $J = (\ker \varphi) R$. It contains the $Z_i$, since $\varphi(Z_i) = 0$.

1. By the Lemma on admissibility, $\mathbf{t}$ followed by $(0, a)$ is admitted for $J$.
2. The element $a$ is a nonzerodivisor modulo $J$: if $ap \in J$, then $\varphi(a) \varphi(p_\mu) = 0$ for every coefficient $p_\mu$ of $p$, and $\varphi(a) \ne 0$ in the domain $L[[\tau]]$. So $\mathbf{t}$ is admitted for $J + aR$, and the lower bound [Theorem 6.11.8](/entry/low-holds/) gives, for large $\mu$,
$$\Bigl(\sum_i c_i\Bigr) 2^{r + r'} \le \chi\bigl(\mathbf{t}, (R/J)/a\bigr)(\mu).$$
3. Since $a$ is a nonzerodivisor on $R/J$, Rule 1 of Proposition 6.11.7 and a reordering of the list give $\chi(\mathbf{t}, (R/J)/a) = \chi(\mathbf{t}(0,a), R/J)$. Rule 3 then gives, for large $\mu$,
$$\chi\bigl(\mathbf{t}, (R/J)/a\bigr)(\mu) \le \chi\bigl(((0, a)), R/(J + (\mathbf{t}))\bigr)(\mu).$$
4. The ideal $J + (\mathbf{t})$ is homogeneous, so the Lemma on the upper bound applies to it: for large $\mu$, the right side of step 3 is at most $2^{r + 1 + r'} \sum_{\xi \in T} v(\xi(a))$.
5. Choose one $\mu$ that is large for steps 2, 3 and 4, and divide by $2^{r + r'}$. $\square$

### The main theorem

**Theorem 6.12.8 (Length bound for the cotangent lattice).** Let $v$ be a valuation normalized on $\mathcal{O}$. Let $A$ be a weighted algebra with a system of equations with counts $(r, s, r', s', m)$ and ideal $I$, and let $a \in A$. Assume M1 to M5. Then:

1. there is a finite set $T$ that covers $S$;
2. the cotangent length $\ell_{-1}(F)$ is finite;
3. for every $T$ that covers $S$,
$$\ell_{-1}(F) \le 2 \sum_{\xi \in T} v(\xi(a)).$$

Lean: `UpperTheory.V.Alg.M.main_holds`, `UpperTheory.V.Alg.LemmaM`.

*Proof.* 1. *The rank.* Since $x$ is smooth with $r$ variables of weight $-1$, the lattice $C_{-1}$ is a free $\mathcal{O}$-module of rank $r$.

2. *Normal form.* The $r + 1$ elements $F_0, \dots, F_r$ span the rank $r$ lattice $C_{-1}$ up to scalars. By the elementary divisor theorem over the discrete valuation ring $\mathcal{O}$, there is a family $F'$ with the same $\mathcal{O}$-span as $F$, elements $y_i \in A_{-1}$ and integers $c_i$ with $F'_i - \varpi^{c_i} y_i \in \mathfrak{s}$ for $i < r$ and $F'_r \in \mathfrak{s}$, where the images of the $y_i$ form a basis of $C_{-1}$. Then $\ell_{-1}(F) = \sum_i c_i$, which is finite. Replacing $F$ by $F'$ does not change $I$, the spanning condition or $\ell_{-1}$.

3. *Removing weight zero.* The chart of M1 has $m$ variables of weight $0$, and the images of $Z_1, \dots, Z_m$ span the weight $0$ cotangent space. By the implicit function theorem for power series over $L$, there is a chart without weight zero, with the other counts unchanged, that kills each $Z_i$.

4. *Moving $a$.* There is $a' \in A_0$ with $a' - a \in I$, $x(a') = x(a)$ and $\varphi(a') \ne 0$. Every point on $S$ takes the same value on $a$ and on $a'$, so $a'$ satisfies M5.

5. *Covering sets.* The ideal $I$ is homogeneous, since its generators are. By M2 the points of $\operatorname{Spec} (A/I)_0$ over $K$ are finite in number, and by M4 the two-signed points over each of them form finitely many orbits. One point from each orbit gives $T$. This proves part 1.

6. *The bound.* The Core bound applied to $F'$, the chart of step 3, the $y_i$, the $c_i$ and $a'$ gives $\sum_i c_i \le 2 \sum_{\xi \in T} v(\xi(a'))$. Since $\xi(a') = \xi(a)$ for $\xi \in T$, this proves part 3. $\square$

Part 1 makes part 3 a statement with content: without a covering set, the bound would say nothing. The factor $2$ comes from the squares $F_i^2$ in the Rees algebra of Section 6.11.

**Remark 6.12.9 (Formalization).** The Core bound takes `IsCO O (𝒜 0)` as an instance argument and also the hypothesis `IsWRing 𝒜 x`, whose field `co` is the same statement; the main theorem obtains the instance from `IsWRing` by `haveI := hW.co` ([MainCotSpan.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/MainCotSpan.lean#L35)). The existence of a covering set uses only M2, M4 and the homogeneity of $I$; M3 is not needed there ([FinHolds.lean](lean:Development/AutomorphicArithmetic/AutomorphicVarieties/CommutativeAlgebra/GradedModulesLength/FinHolds.lean#L49)). The cotangent length has values in `ℕ∞`, and part 3 compares its `toNat` with a real number, so part 2 is needed for part 3 to mean what it says. The spanning condition for $Z$ in M1 is used only in step 3.
