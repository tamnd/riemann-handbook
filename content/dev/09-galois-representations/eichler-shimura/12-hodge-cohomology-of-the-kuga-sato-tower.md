---
title: Hodge cohomology of the Kuga-Sato tower
decls:
  - UpperTheory.Gal.Cnt.weighted_count_definite_unitary
  - UpperTheory.Gal.Cnt.trace_definite_forms_identity
  - UpperTheory.Gal.LocalSmoothExtension.GroupTop_of
  - UpperTheory.Gal.LocalSmoothExtension.hodgeTrace_of_lefschetz_and_groupSide
  - UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_inputs
  - UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_geo
  - UpperTheory.Gal.Int.Geo.kodaira_spencer_of_weight_one
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Hodge cohomology of the Kuga-Sato tower

Section 09 wrote the fixed-point side of the holomorphic Lefschetz formula for a Hecke correspondence on a Kuga-Sato variety as a complex total: a weighted sum over the points of $\mathcal{P}$ fixed by elements of the unitary group. Two results from the trace formula turn that total into a trace on algebraic modular forms for a definite unitary group, and a suitable combination of the twists $\alpha$ makes the weights a Schur polynomial times $\sum_i y^{h_i}$, with $h_i$ the expected Hodge degrees. The Lefschetz formula then reads the Hodge cohomology of the tower, and gives the sixth fact of Section 07: each Hecke eigensystem of weight $\lambda$ occurs in Hodge cohomology in the degrees $h_i$. The section ends with all six facts.

We keep the setting of Sections 08 and 09. Say that the data are *in the standard range* if $a = m = 1$, exactly one infinite place of $F$ has signature one, $n$ is odd, and the moduli problem is compact.

A *similitude pair* is a pair $(\beta, \gamma)$ of units of the central simple algebra of $G$ with $\beta$ hermitian, $\gamma \beta \gamma^* = c\beta$ for some $c \in \mathbb{Q}^\times$, and the minimal polynomial $m_\gamma$ of $\gamma$ over $F$ separable of degree $n$, such that $\beta$ is trivial in the adelic sense away from $p$ and at the real places. A *mark* of the pair is an eigenvalue $\mu$ of $\gamma$ at a place of signature one, on a vector of positive norm for $\beta^{-1}$. The pair is *definite* if, instead of the condition at the real places, $\beta^{-1}$ is positive definite at the place of signature one and negative definite at the others. For a pair, a level $K$ with a function $f$ on $G(\mathbb{A}_f^p)$, and $K' \subseteq G_p$ with a function $f'$, let $O_{\beta,\gamma}(f, f')$ be the orbital sum of $f \otimes f'$ at $\gamma$ on the group of $\beta$, at the trivial twist at $p$. Pairs are classified up to $(\beta, \gamma) \sim (s\, y\beta y^*, y\gamma y^{-1})$ with $s > 0$ rational. For a function $\mathrm{wt}$ on polynomials put
$$S(\mathrm{wt}; K, f, K', f') = \sum_{[\beta, \gamma] \text{ definite},\ m_\gamma \text{ irreducible}} \mathrm{wt}(m_\gamma)\, O_{\beta, \gamma}(f, f').$$

A *definite form* is a hermitian $\beta$ with the positivity condition above and trivial away from $p$. For a representation $\xi$ of the units of the algebra times $\mathbb{Q}^\times$ on a finite-dimensional complex space, let $D(\xi; K, f, K', f')$ be the sum over the classes of definite forms $\beta$ of the trace of the Hecke operator of $f \otimes f'$ on the algebraic modular forms of weight $\xi$ for the group of $\beta$ (B. H. Gross, Algebraic modular forms, Israel J. Math. 113 (1999)), with the convention that the trace is $0$ when the operator is not defined. A function $f$ is a *test function* for $K$ if it is a $K$-bi-invariant function of finite support; at $p$ we use $K_p$ and its indicator $\mathbf{1}_{K_p}$. For a function $c$ of pairs $(P, \mu)$ write $\operatorname{Tot}^{\flat}(c)$ for the complex total of Section 09 with $c(\chi_y, \mu_y(a))$ replaced by $c(m_y, \mu_y(a))$, where $m_y$ is the minimal polynomial of $y$.

**Theorem 3.12.1 (weighted count of marked fixed points).** Suppose that exactly one infinite place of $F$ has signature one and that $n$ is odd, and let $v$ be that place. Let $c$ be any function of pairs $(P, \mu)$, let $K$ be a level and $f$ a test function for $K$ supported on regular elements, and let $f'$ be a test function for $K' \subseteq G_p$. Suppose that every similitude pair with a mark and with $m_\gamma$ reducible has $O_{\beta,\gamma}(f, f') = 0$. Then
$$\operatorname{Tot}^{\flat}(c; K, f, K', f') = S\Bigl(P \mapsto \sum_{r} c(P, r); K, f, K', f'\Bigr),$$
where $r$ runs over the roots of $P$ under $v$, with multiplicity.

Lean: `UpperTheory.Gal.Cnt.weighted_count_definite_unitary`.

We take this as given from other chapters: it combines [the count of regular marked points](/entry/complex-count-regular-marked-points/), the comparison of marked pairs with definite pairs, and the finiteness of the marked classes.

**Theorem 3.12.2 (trace identity on definite forms).** Suppose that exactly one infinite place has signature one. Let $\xi$ be a representation as above and $\mathrm{wt}$ a function on polynomials with $\operatorname{tr} \xi(y) = \mathrm{wt}(m_y)$ for every $y$ in the group of a definite form whose minimal polynomial is separable of degree $n$. Let $f$ be a test function for a level $K$ and $f'$ a test function for $K' \subseteq G_p$, and suppose that the orbital integrals of $f \otimes f'$ vanish at every $y$ whose minimal polynomial is not separable and irreducible of degree $n$. Then
$$S(\mathrm{wt}; K, f, K', f') = D(\xi; K, f, K', f').$$

Lean: `UpperTheory.Gal.Cnt.trace_definite_forms_identity`.

This is the trace formula for a group that is compact at infinity, where the spectral side is a finite trace; we take it as given from [the trace identity on definite forms](/entry/lkdef-trace-definite-forms-identity/).

Now the weights. For $\chi \in F[x]$ and $\lambda = (\lambda_\tau)$, a family of $n$-tuples of non-negative integers indexed by the embeddings $\tau : F \to \mathbb{C}$, let $s_\lambda(\chi) = \prod_\tau s_{\lambda_\tau}(\text{roots of } \chi^\tau)$ if every $\chi^\tau$ has $n$ roots in $\mathbb{C}$, and $s_\lambda(\chi) = 0$ otherwise, with $s_{\lambda_\tau}$ the Schur polynomial. A representation $\xi$ has *weight* $\lambda$ if $\operatorname{tr} \xi(y) = s_\lambda(\chi_y)$ for every $y$ in the group of a definite form with minimal polynomial separable of degree $n$. Write $|\lambda_\tau| = \sum_j \lambda_{\tau, j}$, $\varepsilon_\tau$ as in Section 09, and $\sigma\lambda$ for the family $\tau \mapsto \lambda_{\sigma^{-1} \tau}$, for $\sigma \in \operatorname{Aut}(\mathbb{C})$.

**Definition 3.12.3 (Hodge degrees).** Let $t_0 : F \to \mathbb{C}$ and $\Sigma = \sum_{\tau \neq t_0, \bar t_0} \varepsilon_\tau |\lambda_\tau|$. A tuple $(h_0, \dots, h_{n-1})$ is a list of *Hodge degrees* for $\lambda$ at $t_0$ if either $\lambda_{\bar t_0, i} = m$ for all $i$ and
$$h_i = (n-1)m + \Sigma + \lambda_{t_0, i} + (n - 1 - i),$$
or $\lambda_{t_0, i} = m$ for all $i$ and
$$h_i = m + \Sigma + \sum_{j \neq i} \lambda_{\bar t_0, j} + i.$$

A test function $f$ for $K$ is *good* if it is supported on regular elements, if every marked similitude pair with reducible $m_\gamma$ has $O_{\beta,\gamma}(f, \mathbf{1}_{K_p}) = 0$, and if the orbital integrals of $f \otimes \mathbf{1}_{K_p}$ vanish at every element of the group of a definite form whose minimal polynomial is not separable and irreducible of degree $n$.

**Theorem 3.12.4 (group side of the Hodge trace).** Let $i_0$ be an index and $h$ a list of Hodge degrees for $\lambda$ at $\tau_{i_0}$. There is $k_0$ such that for every $k \geq k_0$ there are coefficients $c_\alpha \in \mathbb{C}$, for finitely many $\alpha \in \mathcal{O}_F^k$, each with all $\alpha_s$ nonzero and divisible by $2$, with the following property. If $a = 1$, exactly one infinite place has signature one, $n$ is odd, $v$ has signature one, $\xi$ has weight $\lambda$, and $f$ is a good function in the Hecke algebra of a level $K$, then for all $y \in \mathbb{C}$
$$\operatorname{Tot}\Bigl(\sum_\alpha c_\alpha\, w^{\tau_{i_0}}_\alpha(y; \chi, \mu^*); K, f, K_p, \mathbf{1}_{K_p}\Bigr) = D(\xi; K, f, K_p, \mathbf{1}_{K_p}) \cdot \sum_{i} y^{h_i}.$$

Lean: `UpperTheory.Gal.LocalSmoothExtension.GroupTop_of`.

*Proof.* The coefficients come from a root identity: for $k$ large there are $c_\alpha$ with
$$\sum_\alpha c_\alpha \sum_{\mu} w^{\tau_{i_0}}_\alpha(y; \chi, \mu) = s_\lambda(\chi) \sum_i y^{h_i}$$
for every $\chi$ of degree $n$, separable, with $\chi(0) \neq 0$ and with all roots of the same absolute value, where $\mu$ runs over the roots of $\chi^{\tau_{i_0}}$. The weight is a product of factors $\phi_{\alpha_s}$, polynomial in the $\tau(\alpha_s)$, and a linear system in the $c_\alpha$ isolates the Schur polynomial. Now apply Theorem 3.12.1 with $c(P, \mu) = \sum_\alpha c_\alpha w_\alpha(y; \chi, \mu^*)$, $\chi$ the monic reciprocal of $P$. Through $\mu \mapsto \mu^*$ the roots of $m_\gamma$ at $v$ become the roots of $\chi^{\tau_{i_0}}$, on one circle since $\gamma$ is a similitude, so the root sum is $s_\lambda(\chi) \sum_i y^{h_i}$. Theorem 3.12.2 with $\mathrm{wt}(P) = s_\lambda(\chi)$, which is the trace of $\xi$, gives $D(\xi)$. $\square$

On the geometric side, let $T$ be a Kuga-Sato tower of power $k$ over a standard base over $\mathbb{C}$ (Section 09) and $Z_N$ its variety at level $N$. For $\alpha \in \mathcal{O}_F^k$ let $\alpha^*$ be the pullback by $\alpha$ acting on the factors, and for coefficients $c$ put $\alpha_c = \sum_\alpha c_\alpha\, \alpha^*$ on Hodge cohomology. For $f$ in the Hecke algebra let $f_*$ be its Hecke operator of Section 05. For $\psi = (\psi_j)$ a family of Hecke functions, $\theta = (\theta_j)$ complex numbers and $f$ a Hecke function, say that $\theta$ is an *eigensystem of weight $\lambda$ detected by $f$* if the $\psi_j$ commute in their action on $f$ and there is $\xi$ of weight $\lambda$ such that for every polynomial $s$ in the $\psi_j$ with $s(\theta) \neq 0$ there is a polynomial $a$ with $f_{as} = (as)(\psi) * f$ good and $D(\xi; K_N, f_{as}, K_p, \mathbf{1}_{K_p}) \neq 0$.

**Theorem 3.12.5 (Hodge trace and Hodge eigenvectors).** Assume the holomorphic Lefschetz formula (Theorem 3.7.2), that every Kuga-Sato variety of a tower in the standard range is projective and smooth of some dimension over $\mathbb{C}$, the fixed-point formula on the tower (Theorem 3.9.6), and the statements of Theorems 1.12.1 and 1.12.2. Then:

1. *(Hodge trace.)* For $i_0$ and $h$ a list of Hodge degrees for $\lambda$ at $\tau_{i_0}$, there is $k_0$ such that for each $k \geq k_0$ there are coefficients $c$ such that, in the standard range, for every tower $T$ of power $k$, level $N$ with $Z_N$ smooth of dimension $d$, $\xi$ of weight $\lambda$, good Hecke function $f$ at level $N$ and $y \in \mathbb{C}$,
$$\sum_{a=0}^{d} (-y)^a \sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(f_* \circ \alpha_c \mid H^b(Z_N, \Omega^a)\bigr) = D(\xi; K_N, f, K_p, \mathbf{1}_{K_p}) \cdot \sum_i y^{h_i}.$$
2. *(Hodge eigenvectors.)* In the standard range, for $\lambda$ with each $\lambda_\tau$ non-increasing there is $k$ such that for every tower $T$ of power $k$, level $N$, $\sigma \in \operatorname{Aut}(\mathbb{C})$, list $h$ of Hodge degrees for $\sigma\lambda$ at $\tau_{i_0}$, and eigensystem $\theta$ of weight $\sigma\lambda$ detected by $f$ (with $f$ and the $\psi_j$ Hecke functions at level $N$), each $h_i$ has some $b$ and a nonzero $x \in H^b(Z_N, \Omega^{h_i})$ with $\psi_{j*} x = \theta_j x$ for all $j$.
3. *(Occurrence.)* The conclusion of Theorem 3.12.6 below holds.

Lean: `UpperTheory.Gal.LocalSmoothExtension.hodgeTrace_of_lefschetz_and_groupSide`.

*Proof.* For 1, write $f$ as a combination of indicators of double cosets $K_N h^{-1} K_N$. For each, the operator $f_* \circ \alpha^*$ on $H^b(Z_N, \Omega^a)$ is the Hodge trace of the correspondence $(\operatorname{tr}_1, \operatorname{tr}_{h,\alpha})$ from level $N'$. By the Lefschetz formula, its alternating sum over $b$ is $\sum_{x \in \Phi} [t^a] \det(1 + tA_x)/\det(1 - A_x)$, so the left side of 1 is $\sum_x \ell(A_x, y)$. Theorem 3.9.6 makes this $[K_{N,h} : K_{N'} \cap K_{N,h}] \cdot \operatorname{Tot}(w_\alpha(y; \chi, \mu^*))$, and the same index relates the correspondence $(\operatorname{tr}_1, \operatorname{tr}_{h,\alpha})$ to the Hecke operator of the double coset. Summing with the $c_\alpha$ of Theorem 3.12.4 gives the right side.

For 2, take $\xi$ for $\sigma\lambda$ and $s$ with $s(\theta) \neq 0$. By 1 with $f_{as}$, the polynomial $\sum_a (-y)^a \sum_b (-1)^b \operatorname{tr}(\cdots)$ has the term $y^{h_i}$ with nonzero coefficient, since $D \ne 0$ and the $h_i$ are distinct: in both cases of Definition 3.12.3 they are strictly monotone in $i$ because $\lambda$ is non-increasing. So some $H^b(Z_N, \Omega^{h_i})$ has nonzero trace for $f_{as} \circ \alpha_c$. These spaces are finite-dimensional, and the commuting operators $\psi_{j*}$ split them into generalized eigenspaces. Since this holds for every $s$ with $s(\theta) \ne 0$, the eigenvalue $\theta$ occurs, and a common eigenvector exists in degree $h_i$.

For 3, base change of the tower along $\tau$ and the conjugation by $\sigma$ (Theorem 3.5.2) move the eigenvectors of 2 to the tower over $R$, which is the Hodge occurrence of Section 05. $\square$

**Theorem 3.12.6 (Hodge occurrence on the tower).** Assume the holomorphic Lefschetz formula and the fixed-point formula on the tower. Suppose the data are in the standard range, and let each $\lambda_\tau$ be non-increasing. Then there is $k$ such that the following holds. Let $R$ be a field of characteristic $0$ with a base, $T$ a Kuga-Sato tower of power $k$ over it, $N$ a level, $(g_j)$ members of the Hecke algebra at $N$ with eigenvalues $\theta_j \in \mathbb{C}$, and $f$ a Hecke function of the tower such that $\theta$ is an eigensystem of weight $\lambda$ detected by $f$. Let $\tau : R \to \mathbb{C}$ with $\tau(\rho)$ the fixed complex value and $\tau \circ t_i = \tau_i$, let $\sigma \in \operatorname{Aut}(\mathbb{C})$, let $i_0$ be an index, and let $h$ be a list of Hodge degrees for $\sigma\lambda$ at $\tau_{i_0}$. Then for each $i$ the eigensystem $\sigma \circ \theta$ occurs in Hodge degree $h_i$ in the base change of the Hecke tower of $(T, N, g)$ along $\tau$.

Lean: `UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_geo` (also `UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_inputs`).

*Proof.* The Kuga-Sato varieties over $\mathbb{C}$ are projective and smooth, as fibre powers of abelian schemes over the smooth models, projective over a compact base. With Theorems 1.12.1 and 1.12.2, all hypotheses of Theorem 3.12.5 hold, and its third part is the claim. $\square$

**Theorem 3.12.7 (six facts on the Kuga-Sato tower).** Assume the holomorphic Lefschetz formula. Then:

1. if $a = 1$, for every number field $E$ and isomorphism $F \cong E$ there is a standard base over $E$;
2. in the standard range, a Kuga-Sato tower of each power $k$ exists over every field of characteristic $0$ with any base;
3. in the standard range, the Hecke towers of a Kuga-Sato tower are nice;
4. in the standard range, for a standard base over a number field $E$ and a place $w$ of $E$ over a prime $\mathfrak{w}$ of $F$, if the eigensystem satisfies the group conditions for good reduction at $\mathfrak{w}$, the Hecke tower has a good model at $w$;
5. under the same assumptions with the group conditions for a congruence relation at $\mathfrak{w}$ with coefficients $\vartheta$, the Hecke tower has a congruence model at $w$ with these coefficients;
6. the Hodge occurrence of Theorem 3.12.6 holds.

Lean: `UpperTheory.Gal.Int.Geo.kodaira_spencer_of_weight_one`.

*Proof.* Items 1 and 5 follow from [the integral models of the Kuga-Sato tower](/entry/m-in/), item 5 through the congruence relation of Theorem 3.11.4 on the finite étale level models. Item 2 is [the existence of Kuga-Sato towers](/entry/k-sex-holds/), item 3 is the niceness of their Hecke towers, and item 4 is [the good models at good places](/entry/ks-good-holds/). Item 6 is Theorem 3.12.6, with the fixed-point formula of Theorem 3.9.6. $\square$

**Remark 3.12.8 (Formalization).** `ksHodge_of_geo` supplies `weighted_count_definite_unitary` and `trace_definite_forms_identity` to `ksHodge_of_inputs`, which supplies the projectivity fact `KSProj_holds` to `hodgeTrace_of_lefschetz_and_groupSide` and keeps only its third component; `HodgeTr` and `HodgeEig` are used only to reach `KSHodge`. `trace_definite_forms_identity` is an alias of `GlobalTheory.LKDef.trace_definite_forms_identity`, and `heckeTrace` is $0$ when no operator exists. `schW` is $0$ when $\chi$ does not split. The theorem `kodaira_spencer_of_weight_one` is about Kuga-Sato varieties, not a Kodaira-Spencer map; it is the structure `KSAll` built from `stdEx_holds`, `kSEx_holds`, `kSNice_holds`, `ksGood_holds`, `ksCong_holds` and `ksHodge_of_geo hW FixK_holds`.
