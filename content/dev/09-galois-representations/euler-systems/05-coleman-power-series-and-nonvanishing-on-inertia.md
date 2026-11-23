---
title: Coleman power series and nonvanishing on inertia
decls:
  - UpperTheory.Kd.C7.pRepEx
  - UpperTheory.Kd.C7.pCore
  - UpperTheory.Kd.C7.LocalUnitsRoots.main
  - UpperTheory.Kd.C7.pLocu
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Coleman power series and nonvanishing on inertia

This section proves that the global class $y$ of an Euler system does not vanish on the inertia group at $\ell$. The tool is Coleman's power series for norm-compatible units [Coleman 1979]. A norm-compatible family of Kummer cocycles on inertia comes, level by level, from units $P(\zeta_{\ell^m})$. We find one power series over a large unramified ring whose logarithmic derivative gives all these units at once. A suitable combination of these series is a power series $G$ with integral coefficients. If $y$ vanished on inertia, the moments of $G$ would vanish. A transfer of nonvanishing from a second series $L$ shows that they do not. The result is one of the two halves of [the unramified zeta theorem](/entry/zeta-ur/). The background is in [local fields](/learn/galois-cohomology/#local-fields), [Iwasawa theory](/learn/galois-cohomology/#iwasawa-theory) and [the cyclotomic character](/learn/galois-representations/#the-cyclotomic-character-and-tate-modules).

### Kummer presentations

Fix an odd prime $\ell$, an algebraic closure $\Omega$ of $\mathbb{Q}$, and a valuation ring $A$ of $\Omega$ that lies over $\ell$. Let $I_A$ and $D_A$ be its inertia and decomposition groups, $\chi_m$ the [[cyclotomic character|XSGB5K2KEG]] mod $\ell^m$, and $H_m = I_A \cap \ker \chi_m$. Let $R_0 \subseteq A$ be the ring of elements of $A$ fixed by $I_A$. For $x, x' \in \overline{\mathbb{Q}}_\ell$ write $x \equiv_n x'$ when $|x - x'| \leq |\ell^n|$. A *coefficient datum* has a ring $\mathcal{O} \subseteq \overline{\mathbb{Q}}_\ell$; a *basis* of it is a $\mathbb{Z}_\ell$-basis $\beta_1, \ldots, \beta_d$ of $\mathcal{O}$.

**Definition 5.5.1.** A *system* is a family $Z_r \colon G_{\mathbb{Q}} \times (\mathbb{Z}/\ell^r)^\times \to \overline{\mathbb{Q}}_\ell$. It is an *inertia system* if, for $s, t \in I_A$: $Z_r(s, x) \in \mathcal{O}$; $Z_r(st, x) = Z_r(s, x) + Z_r(t, x\chi_r(s)^{-1})$; and $Z_r(s, x)$ is the sum of $Z_{r+1}(s, x')$ over the $x'$ above $x$.

**Definition 5.5.2.** Let $\zeta$ be a primitive $\ell^n$-th root of unity, $n \leq r$, $u_1, \ldots, u_k$ units of $A$ and $o_1, \ldots, o_k \in \overline{\mathbb{Q}}_\ell$ with $|o_i| \leq 1$. These form a *Kummer presentation* of $Z_r$ at precision $n$ if, for each $s \in I_A$ with $\chi_r(s) = 1$ and $s\zeta = \zeta$, there are $k_i \in \mathbb{Z}/\ell^n$ and roots $v_i^{\ell^n} = u_i$ with $s v_i = \zeta^{k_i} v_i$ and $Z_r(s, 1) \equiv_n \sum_i o_i k_i$.

Fix a compatible family $\zeta_m$ of primitive $\ell^m$-th roots of unity, with $\zeta_{m+1}^\ell = \zeta_m$. A tuple $P_1, \ldots, P_d$ of polynomials over $R_0$ is a *basis presentation* of $Z$ at level $m$ and precision $n$ if $P_i(\zeta_m)$, with the weights $\beta_i$ and the root $\zeta_n$, is a Kummer presentation of $Z_m$ at precision $n$. The system $Z$ *has presentations* if there are $c_0$ and $m_0$ with a basis presentation at level $m$ and precision $m - c_0$ for each $m \geq m_0$.

### Frames and Coleman series

**Definition 5.5.3.** A *frame* for $A$ and an embedding $j \colon \Omega \to \overline{\mathbb{Q}}_\ell$ is a $\mathbb{Z}_\ell$-algebra $R$ with these data:

1. an automorphism $\sigma$ that lifts Frobenius: $R$ is a domain, $\ell$ is prime in $R$, $R$ is $\ell$-adically complete, $\sigma(x) \equiv x^\ell \bmod \ell$, and each element is an $\ell$-th power mod $\ell$;
2. monic polynomials of positive degree have roots mod $\ell$; elements outside $\ell R$ are units; elements fixed by $\sigma$ come from $\mathbb{Z}_\ell$;
3. a map $i_0 \colon R_0 \to R$ with dense image, such that $i_0(y) \in \ell^n R$ implies $y \in \ell^n R_0$;
4. a Frobenius element $\mathrm{fr} \in D_A$ with trivial Teichmüller character and $\sigma(i_0 y) = i_0(\mathrm{fr}\, y)$;
5. a map $j_h \colon R \to \mathbb{C}_\ell$ with $|j_h| \leq 1$, compatible with $j$ and with $\mathbb{Z}_\ell$.

For a polynomial $P$ over $R_0$ put $\mathrm{ser}(P) = P(1 + X) \in R[[X]]$. For $f \in R[[X]]$ let $\mathrm{dl}(f) = f'/f$ when $f$ is a unit, and $f^{(m)}$ the series with $\sigma^{-m}$ applied to the coefficients. The *evaluation at level $m$* is the map $R[[X]] \to R[[X]]/(\Phi_{\ell^m}(1+X))$, where $\Phi_{\ell^m}$ is the cyclotomic polynomial. Write $f \equiv_{m,n} g$ if the two evaluations at level $m$ differ by a multiple of $\ell^n$.

**Definition 5.5.4.** A tuple $D_1, \ldots, D_d$ in $R[[X]]$ is a *Coleman vector* for $Z$ if there are $c_1, m_1$ such that for each $m \geq m_1$ there is a basis presentation $P$ of $Z$ at level $m$ and precision $m - c_1$ with $D_i^{(m)} \equiv_{m, m - c_1} \mathrm{dl}(\mathrm{ser}(P_i))$ for each $i$.

**Theorem 5.5.5 (existence of Coleman vectors).** Let $\ell \neq 2$ be prime, $A$ a valuation ring over $\ell$, $j$ an embedding, $R$ a frame, $\beta$ a basis of a coefficient datum and $(\zeta_m)$ a compatible family. Every inertia system $Z$ that has presentations has a Coleman vector.

Lean: `UpperTheory.Kd.C7.pRepEx`

*Proof.* Let $c_0, m_0$ come from the presentations, and choose a basis presentation $P^{(m)}$ for each $m \geq m_0$. Put $c = c_0 + 1$ and $M = \max(m_0, c)$.

1. For $m \geq M$, each $P^{(m)}_i(\zeta_m)$ is a unit of $A$. Then $\mathrm{ser}(P^{(m)}_i)$ is a unit of $R[[X]]$.
2. Lower the precision of $P^{(m+1)}$ to $m - c_0$. The two presentations at levels $m+1$ and $m$ give a unit $Q(\zeta_m)$ with $\prod_{x \equiv 1 \bmod \ell^m} P^{(m+1)}_i(\zeta_{m+1}^x) = P^{(m)}_i(\zeta_m)\, Q(\zeta_m)^{\ell^{m - c}}$.
3. A product of values over the roots above $\zeta_m$ is the norm from level $m+1$ to level $m$. So the norm of $\mathrm{ser}(P^{(m+1)}_i)$ is $\mathrm{ser}(P^{(m)}_i)\,\mathrm{ser}(Q)^{\ell^{m-c}}$ at level $m$.
4. Coleman's theorem in this frame then gives a unit $f_i \in R[[X]]$ such that for each $m \geq M$ and $N$ there is a unit $w$ with $f_i^{(m)} \equiv_{m,N} \mathrm{ser}(P^{(m)}_i)\, w^{\ell^{m-c}}$.
5. Put $D_i = \mathrm{dl}(f_i)$. Twisting by $\sigma^{-m}$ commutes with $\mathrm{dl}$ on units. If $F \equiv_{m,N} g\, w^{\ell^n}$, then $\mathrm{dl}\, F \equiv_{m, \min(n, m-1, N)} \mathrm{dl}\, g$. With $n = m - c$ and $N = m$ this gives precision $m - c$, and $P^{(m)}$ is a basis presentation at precision $m - c$. So $D$ is a Coleman vector with $c_1 = c$ and $m_1 = M$. $\square$

### The Coleman core

For a series $L$ over $\overline{\mathbb{Q}}_\ell$ let $\mathrm{tv}_m(L)(z) = \sum_{n < \ell^{3m}} L_n (z-1)^n$. For a character $\varphi$ mod $\ell$, $k \in \mathbb{N}$ and a primitive $\ell^r$-th root $\xi$, the *moment* is
$$I_r(L; \xi) = \sum_{0 < x < \ell^r,\ \ell \nmid x} \varphi(x)\, x^k \sum_{t < \ell^r} \xi^{-tx}\, \mathrm{tv}_r(L)(\xi^t).$$
We say *the moments of $L$ vanish* if for each $n$, for all large $r$ and all $\xi$, $I_r(L; \xi) \equiv_{n+r} 0$. We say *the twisted sums of $Z$ vanish* if for each $n$, for all large $r$ and each $s \in I_A$ with trivial Teichmüller character, $\sum_x \varphi(x)^{-1} x^{-k} Z_r(s, x) \equiv_n 0$. For polynomials $P_i$, weights $o_i$ and $b \in \mathbb{N}$ put
$$h(b) = \sum_i o_i\, j\Bigl( \frac{\zeta^b P_i'(\zeta^b)}{P_i(\zeta^b)} \Bigr).$$

**Theorem 5.5.6 (Coleman core).** Let $\ell \neq 2$, $A$ over $\ell$, $Z$ an inertia system, $a \in \overline{\mathbb{Q}}_\ell$ with $|a| = 1$, $j$ an embedding with $|j| \leq 1$ on $A$, $\ell \nmid d_0$, and $(\zeta_m)$ a compatible family. Assume $Z_m(\sigma s \sigma^{-1}, 1) = a Z_m(s, 1)$ for each Frobenius $\sigma \in D_A$ with trivial Teichmüller character, each $m$ and each $s \in H_m$. Assume that for $m \geq m_0$, $Z_m$ has a Kummer presentation at precision $m - e_0$ with root $\zeta_{m - e_0}$, by values $P_i(\zeta_m)$ of polynomials with coefficients in $R_0$ and weights $o_i \in \mathcal{O}$. Then there are a series $G$ with coefficients in $\mathcal{O}$, units $v_m$ with $v_{m+1} \equiv_m v_m$, and $c_1, m_1$ such that:

1. for $m \geq m_1$, each such presentation and each character $\psi$ mod $\ell^m$,
$$\begin{aligned} \bigl(1 - d_0 \psi^{-1}(d_0)\bigr) \sum_b \psi(b)\, h(b) \equiv_{m - c_1} v_m a^m \sum_b \psi(b)\, \mathrm{tv}_m(G)\bigl(j(\zeta_m)^b\bigr); \end{aligned}$$
2. for each $\varphi$ mod $\ell$ and $k \geq 1$, if the twisted sums of $Z$ vanish, the moments of $G$ vanish.

Lean: `UpperTheory.Kd.C7.pCore`

*Proof.* The proof has these steps.

1. A frame $R$ exists, and the coefficient datum has a basis $\beta$. Each presentation can be rewritten in the basis, with the same values of $h$ mod $\ell^n$. So $Z$ has presentations.
2. Put $Z^\sharp(x) = Z(x) - d_0 Z(d_0 x)$. It is again an inertia system with presentations. The previous theorem gives a Coleman vector $D$ for $Z^\sharp$.
3. The Frobenius law moves to $Z^\sharp$. On Coleman vectors it reads $D^{(1)} = M_a D$, with $M_a$ the matrix of multiplication by $a$ in the basis. A solution of this linear Frobenius equation is a unit $v \in \mathbb{C}_\ell$ times a vector with entries in $\mathcal{O}$. This gives $G$ with $\sum_i \beta_i D_{i,n} = v\, G_n$. Approximate $v$ by algebraic units $v_m$.
4. Clause 1 follows by evaluation at $j(\zeta_m)^b$. The factor $1 - d_0 \psi^{-1}(d_0)$ comes from $Z^\sharp$.
5. For clause 2, a division lemma gives $g$ prime to $\ell$, $c_2$ and an inertia system $Z'$ with $\ell^{c_2} Z = Z'(g\,\cdot) - \theta Z'$ on $H_m$, where $\theta = \varphi(g) g^k$. If $\theta \in \mathcal{O}$, the relation passes to Coleman vectors and to $G$, and the moments of $G$ vanish. Otherwise $Z'^\sharp = 0$, so $Z^\sharp = 0$ on $H_m$ and $G = 0$. $\square$

### Nonvanishing on inertia

**Definition 5.5.7.** Let $W$, $e$, $\mathcal{O}$, a function $\nu$ on $G_{\mathbb{Q}}$, characters $\chi_r$ on $(\mathbb{Z}/\ell^r)^\times$ and a system $Z$ be given. They have *Coleman data* if there are $a, a', \kappa \in \overline{\mathbb{Q}}_\ell$, units $v'_m$, an embedding $j$, a series $L$, a character $\varphi$ mod $\ell$ and $m_0, c_0, n_0$ with:

1. $\nu = 1$ on $I_A$, and $\nu(\sigma_0) = a$ at some Frobenius element $\sigma_0 \in D_A$;
2. $|a| = |a'| = 1$, $v'_{m+1} \equiv_m v'_m$, $\kappa \neq 0$, $|j| \leq 1$ on $A$, and $L$ has coefficients in $\mathcal{O}$;
3. there are a compatible family $(\zeta_m)$ and a function $\mathrm{Rhs}$ such that for $m \geq m_0$, $Z_m$ has a Kummer presentation at precision $m - c_0$ with root $\zeta_m^{\ell^{c_0}}$, by values $P_i(\zeta_m) \neq 0$ and weights $o_i$ as in the Coleman core, with $\sum_b \psi(b) h(b) \equiv_{m - c_0} \mathrm{Rhs}(m, \psi, j(\zeta_m))$ for each primitive $\psi$ mod $\ell^m$;
4. for $m \geq m_0$, each primitive $\psi$ mod $\ell^m$ and each primitive $\ell^m$-th root $z$, $\mathrm{Rhs}(m, \psi, z) \equiv_{m - c_0} v'_m \kappa\, a'^m \sum_b \psi(b)\, \mathrm{tv}_m(L)(z^b)$;
5. $\chi_r(x) = \varphi(x)^{-1}$ for $r \geq 1$, and $I_r(L; \xi) \not\equiv_{n_0 + r} 0$ for all large $r$ and all $\xi$, with $k = e$.

**Definition 5.5.8.** Let $W$ be a [[Galois representation|JQEYEQJY2G]] of dimension 2 and $y \colon G_{\mathbb{Q}} \to \overline{\mathbb{Q}}_\ell^2$. The pair $(W, y)$ is an *Euler system class* for a coefficient datum and a finite set $S'$ of places if the entries of $W$ and of $y$ lie in $\mathcal{O}$, $y$ is a cocycle for $W$, $y$ is a coboundary on an inertia group at each place prime to $\ell$, and $y$ has tame classes at the places $w \notin S'$ with $\ell^n \mid w - 1$, as in [the previous section](/entry/k4-top/). A system $Z$ is an *Iwasawa system* for $\nu$ if $\nu$ is multiplicative on $D_A$, the values of $Z$ lie in $\mathcal{O}$, $Z_r(st, x) = Z_r(s, x) + \nu(s) Z_r(t, x\chi_r(s)^{-1})$ for $s, t \in D_A$, and the norm relation holds. It is *linked* to $y$ with weight $e$ if for each $n$, for all large $r$ and each $s \in I_A$ with trivial Teichmüller character, $y(s)_2 \equiv_n \sum_x x^{-e} \chi_r(x) Z_r(s, x)$, with $x$ read as its least positive residue.

**Theorem 5.5.9 (nonvanishing from two inputs).** Assume (Transfer): if $\ell \neq 2$, $e \geq 1$, $m_0 \geq 2$, $G$ and $L$ have coefficients in $\mathcal{O}$, $|a| = |a'| = 1$, $\kappa \neq 0$, $v_m$ and $v'_m$ are units with $v_{m+1} \equiv_m v_m$ and the same for $v'$, $c \geq 2$ with $\ell \nmid c$, and for each $m \geq m_0$ there is a primitive $\ell^m$-th root $z$ with
$$\begin{aligned} &\bigl(1 - c\,\psi^{-1}(c)\bigr)\, v'_m \kappa\, a'^m \sum_b \psi(b)\, \mathrm{tv}_m(L)(z^b) \\ &\quad \equiv_{m - c_1} v_m a^m \sum_b \psi(b)\, \mathrm{tv}_m(G)(z^b) \end{aligned}$$
for each primitive $\psi$ mod $\ell^m$, and if $I_r(L; \xi) \not\equiv_{n_0 + r} 0$ for all large $r$ and all $\xi$, then there is $n_1$ with $I_r(G; \xi) \not\equiv_{n_1 + r} 0$ for all large $r$ and all $\xi$. Assume (Quotient): for each newform-type representation $W$ with an unramified source, $W(s)_{22} = 1$ for each $s \in I_A$ with trivial Teichmüller character. Let $W$ be a newform-type representation with an unramified source $g$ of weight $2e + 1$. Let $(W, y)$ be an Euler system class, and let $Z$ be an Iwasawa system for $\nu$, linked to $y$ with weight $e$, with Coleman data. Then there is $s \in I_A$ with trivial Teichmüller character, $W(s)_{22} = 1$ and $y(s)_2 \neq 0$.

Lean: `UpperTheory.Kd.C7.LocalUnitsRoots.main`

*Proof.* Suppose not. By (Quotient), $y(s)_2 = 0$ for all $s \in I_A$ with trivial Teichmüller character. With the link and $\chi_r = \varphi^{-1}$, the twisted sums of $Z$ vanish for $k = e$. Since $\nu = 1$ on $I_A$, $Z$ is an inertia system. Two Frobenius elements differ by an element of $I_A$, so the Iwasawa law gives the Frobenius law with eigenvalue $a$. The Coleman core with $d_0 = 2$ gives $G$. Multiply the congruence of Coleman data by $1 - 2\psi^{-1}(2)$, of norm at most 1, and chain it with clause 1 of the core. Then (Transfer) with $c = 2$ says that the moments of $G$ do not vanish. Clause 2 of the core says that they vanish. $\square$

**Theorem 5.5.10 (nonvanishing on inertia).** Under the hypotheses of the previous theorem without (Transfer) and (Quotient), the same conclusion holds.

Lean: `UpperTheory.Kd.C7.pLocu`

*Proof.* (Transfer) is a transfer theorem for moments of power series, and (Quotient) is a theorem on the quotient character of $W$ on inertia. Apply the previous theorem. $\square$

**Remark 5.5.11 (Formalization).** The existence of Coleman vectors is in [SerMulPow.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/SerMulPow.lean#L31). Below $m_0$ the choice of presentations takes the dummy value `fun _ => 0` at line 40, which is never used. Steps 1 to 5 use `pWD`, `pPresMono`, `pNormGal`, `pNormLev`, `pExact` and `pDlogCmp`, and the private helpers at lines 11 and 24. The Coleman core is in [MemOfMulMem.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/MemOfMulMem.lean#L253); the file is named after the helper `mem_of_mul_mem` at line 92. Its steps use `pFrEx3`, `pBasEx`, `pToBasis`, `pContOf`, `pIwOps`, `pKumEx`, `sharp_eig` (line 132), `pack` (line 140), `exists_approx` (line 177), `pClause1`, `pDiv` and `pClause2`. We have not unfolded `pExact`, `pClause1`, `pClause2` or `pDiv`. In clause 1, $\psi$ need not be primitive. The frame is `Fr` and the Coleman vector is `Rep` ([FrobeniusCompatInclusion.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/FrobeniusCompatInclusion.lean#L23)). The nonvanishing from two inputs is `private`, at [NormFactorLeOne.lean](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L99), with (Transfer) and (Quotient) as `h48` and `h50` at lines 100 and 101. Its statement is `ZetaEulerSystemNonvanishing Pin7`; Coleman data are `Pin7` ([HTPresNuOfPolys.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/HTPresNuOfPolys.lean#L24)), and the Euler system class, the Iwasawa system and the link are `Sys`, `IwSys2` and `SpLink` ([IsLocallyConstantCycMod.lean](lean:Development/AbelianVarietyTheory/Definitions/Foundations/IsLocallyConstantCycMod.lean#L13)). The letter `c₀` has two uses there: a loss of precision in `Pin7`, and the integer 2 of the Euler factor in `h48` (line 144). The last theorem is at [line 162](lean:Development/AutomorphicArithmetic/Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean#L162). It fills `h48` with `GlobalTheory.T.nonvanishing_transfer_characterSums_powerSeries` and `h50` with `GlobalTheory.T.quotient_char_trivial_inertia_cyclotomic_tower`; we have not opened their proofs.
