---
title: Test functions with a spectral property
decls:
  - UpperTheory.Gal.Spc.specOfF
  - UpperTheory.Gal.Spc.specData
  - UpperTheory.Gal.Spc.specTopG
  - UpperTheory.Gal.Int.Geo.Pl.specTop_holds
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Test functions with a spectral property

Theorem 3.12.6 puts an eigensystem $\theta$ into the Hodge cohomology of the Kuga-Sato tower when $\theta$ is an eigensystem of weight $\lambda$ detected by a test function $f$ (Section 12). This section makes such an $f$ for the eigensystems that plans use: Hecke operators of type $i$ at split places, with eigenvalues from the Satake parameters of $U$, and deck elements, with eigenvalue $1$. The function is $u^{*m} * e$, the $m$-fold convolution of one Hecke operator $u$ applied to an idempotent $e$ that comes from a type at $w_0$. Theorem 3.15.2 is a general statement on the definite side. Theorem 3.15.5 checks its hypotheses for a frame and a vector, and Theorem 3.15.6 chooses an auxiliary prime and the type. Section 16 uses the result, Theorem 3.15.7, as the spectral input of plans.

We keep the notation of Sections 12 and 14. For an open compact $K$, let $\mathcal{H}(K)$ be the Hecke algebra of $K$-bi-invariant functions of finite support on $G(\mathbb{A}_f^p)$ with convolution $*$. For a definite form $\beta$ and a representation $\xi$, let $M_\beta(\xi, K)$ be the space of algebraic modular forms of weight $\xi$ for the group of $\beta$ at level $K \times K_p$, and let $f \mapsto f_\beta$ be the action of $\mathcal{H}(K)$ on it. For a family $\psi = (\psi_j)_{j \in J}$ in $\mathcal{H}(K)$ and a polynomial $s$ in noncommuting variables $X_j$, write $s(\psi)$ for the corresponding sum of convolution words and $s(\theta)$ for its value at numbers $\theta_j$.

### The spectral statement

**Definition 3.15.1 (Hecke relations and eigenvectors).** Let $\psi = (\psi_j)$ and $e, u, u'$ be in $\mathcal{H}(K)$. They satisfy the *Hecke relations* if

1. $e * e = e$, $e * \psi_j * e = \psi_j * e$ and $e * u * e = u * e$;
2. $\psi_i * \psi_j * e = \psi_j * \psi_i * e$ and $u * \psi_j * e = \psi_j * u * e$ for all $i, j$;
3. $u' * u * e = e$.

Numbers $\theta = (\theta_j)$ have an *eigenvector* for $(\xi, \psi, e)$ at level $K$ if there are a definite form $\beta$ and a nonzero $\Phi \in M_\beta(\xi, K)$ with $e_\beta \Phi = \Phi$ and $(\psi_j)_\beta \Phi = \theta_j \Phi$ for all $j$.

Lean: `UpperTheory.Gal.Spc.Rel` (also `UpperTheory.Gal.Spc.HasEig`).

So $e$ cuts out a space on which the $\psi_j$ commute with each other and with $u$, and $u$ is invertible on it with inverse $u'$.

**Theorem 3.15.2 (detection from an eigenvector).** Let $G$ be a group as in Section 08 with $a = 1$ and $K$ a level. Let $k$ be a nonarchimedean local field and suppose $G(\mathbb{A}_f^p) \cong \mathrm{GL}_n(k) \times H$ for a group $H$, compatibly with $K$. Call a Hecke function *cuspidal* if its integrals along the unipotent radicals of the proper parabolic subgroups of $\mathrm{GL}_n(k)$ vanish. Suppose that there are finitely many classes of definite forms. Let $\xi$ have weight $\lambda$, and let $\psi, e, u, u'$ in $\mathcal{H}(K)$ satisfy the Hecke relations, with $e$ cuspidal. Suppose that for each $m \ge 1$ there is a set $A_m$ of regular elements whose components in $\mathrm{GL}_n(k)$ have separable characteristic polynomial, such that $A_m$ contains the support of $u^{*m} * e$ and $a A_m \subseteq A_m$ for every $a$ in the support of some $\psi_j$. If $\theta$ has an eigenvector for $(\xi, \psi, e)$ at level $K$, then there is $m \ge 1$ such that $\theta$ is an eigensystem of weight $\lambda$ detected by $u^{*m} * e$.

Lean: `UpperTheory.Gal.Spc.specOfF`.

*Proof.* Fix $m$ (chosen in the third step) and put $f = u^{*m} * e$ and $f_{s} = s(\psi) * f$ for a polynomial $s$. These functions lie in $\mathcal{H}(K)$, and by the relations the $\psi_j$ commute in their action on $f$.

First, each $f_s$ is good. Cuspidal functions form a left ideal of $\mathcal{H}(K)$, so $f$ and $f_s$ are cuspidal. The support of $f_s$ lies in $A_m$, since $A_m$ contains the support of $f$ and is stable under the supports of the $\psi_j$. So $f_s$ is supported on regular elements with separable characteristic polynomial at $k$. A cuspidal function at $k$ has vanishing orbital integrals at elements whose characteristic polynomial at $k$ is separable and reducible, since such an element lies in a proper Levi subgroup. An element of a similitude pair with reducible minimal polynomial, or an element of the group of a definite form whose minimal polynomial is not irreducible of degree $n$, is of this kind. This gives the last two conditions of goodness.

Second, move to linear algebra. Let $\beta_1, \dots, \beta_r$ represent the classes of definite forms and put $W_q = M_{\beta_q}(\xi, K)$. Each $W_q$ is finite-dimensional, since a form is fixed by its values at a set of representatives of the finitely many double cosets. The Hecke action is an algebra homomorphism, so the operators $T_{q,j} = (\psi_j)_{\beta_q}$, $e_q$, $u_q$, $u'_q$ satisfy the Hecke relations in $\operatorname{End}(W_q)$. The eigenvector can be moved to one of the representatives, so some $W_{q_0}$ holds $x \ne 0$ with $e x = x$ and $T_j x = \theta_j x$.

Third, on $W = \bigoplus_q W_q$ put $t_j = T_j e$ and $v = u e$. The $t_j$ commute with each other, with $v$ and with $e$. There is a polynomial $a$ with $a(\theta) = 1$ such that $P = a(t)$ is an idempotent and $(t_j - \theta_j)^{N} P = 0$ for some $N$; $P$ is the projection onto the generalized $\theta$-eigenspace. Then $P e x = x$, so $P e \ne 0$. On the image of $P e$ the operator $v$ is injective, since $u' v = e$ there, so $v$ is invertible on this nonzero finite-dimensional space. If all traces of $v^m$, $m \ge 1$, vanished there, then by Newton's identities all eigenvalues of $v$ would be $0$. So there is $m \ge 1$ with $\operatorname{tr}(P v^m e) \ne 0$.

Fourth, let $s(\theta) \ne 0$. By the relations $u^m e = v^m e$, so the trace of the Hecke operator of $f_{as}$ on $W$ is $\operatorname{tr}(a(t)\, s(t)\, v^m e)$. On the image of $P$ each $t_j - \theta_j$ is nilpotent and commutes with $v^m e$, so this trace is $s(\theta) \operatorname{tr}(P v^m e) \neq 0$. Since $D(\xi; K, f_{as}, K_p, \mathbf{1}_{K_p})$ is the sum over the classes of the traces on the $W_q$, it is nonzero. $\square$

### Auxiliary primes and seen eigenvalues

Now fix a setup $S$ for $(A, n, p)$ with group $G$, a frame $F$ with map $j$ and transpose inverse $\vartheta$, and a vector $V$ for $(x, U, w_0, \mathrm{Up})$ with weight $\lambda$ (Section 14). Write $S_V$ for the finite set of places of $V$ and $\prod_{w \in S_V} K_w$ for its level. Let $\xi_V$ be the representation of $\mathrm{GL}_n(E) \times \mathbb{Q}^\times$ attached to the weight $(W, j_z)$ of $V$, and $\xi_V^\vartheta$ its composition with $(g, t) \mapsto ({}^t g^{-1}, t^{-1})$. Two places are *apart* if they lie over different places of $E^+$.

**Definition 3.15.3 (auxiliary choice).** An *auxiliary choice* for $(S, V)$ is a prime $r$ with a nonempty finite set $W$ of split places prime to $p$ such that $r \neq p$, $r$ is good for $A$, $r$ is prime to every place of $S_V$, every $w \in W$ lies over $r$, every place over $r$ is $w$ or $c(w)$ for some $w \in W$, and the members of $W$ are pairwise apart.

Lean: `UpperTheory.Gal.Spc.SlopeTestRemainingChoices` (also `UpperTheory.Gal.Spc.Half`).

The places of $W$ carry the regularity condition: an element whose components at all places over $r$ have separable characteristic polynomial is regular, and by the conjugation symmetry it is enough to look at the places of $W$.

**Definition 3.15.4 (seen eigenvalues).** An element $k \in G(\mathbb{A}_f^p)$ is *stable* if $k = j(k')$ with $\vartheta(k')$ in the level of $V$ and $\chi(\vartheta(k')_{w_0}) = 1$. For a prime $r_0$ and a level $N$, a Hecke element $g$ at level $N$ with a number $\theta$ is *seen* if either

1. $g$ is a deck element with stable element $h \in K_{r_0}$, and $\theta = 1$; or
2. there are a split place $w$ with $w, c(w) \notin S_V$ and not related to $S_V$ through $x$, a site $\sigma$ of $N$ at $w$ over a good prime different from $r_0$ whose level group consists of stable elements, an index $i \le n$ and Satake parameters $B$ of $U$ at $w$, such that the element of $g$ is $j(\mathrm{diag}(\varpi, \dots, \varpi, 1, \dots, 1) z^i)$ with $i$ entries $\varpi$, a uniformizer at $w$, and a central $z$ attached to $x$, the level of $g$ is $N \cdot N(w)^i$, and
$$\theta = [K_N : K_N \cap h K_N h^{-1}] \cdot \mathrm{sat}_i(N(w), B) \cdot \kappa(w)^{-i},$$
where $\mathrm{sat}_i$ is the eigenvalue of the $i$-th unramified Hecke operator on the representation with Satake parameters $B$.

Lean: `UpperTheory.Gal.Int.Geo.Pl.Seen` (also `UpperTheory.Gal.Int.Geo.Pl.Stab`).

Case 2 is the Hecke operator $T_i$ at $w$, twisted by the Hecke character $\kappa$ of $V$, with the eigenvalue normalized by the Satake parameters of $U$.

### Building the test function

**Theorem 3.15.5 (test functions from a type).** Let $n$ be odd, suppose $S$ is in the standard range, $\omega$ and $x$ generate the same field, $S_V$ is prime to $p$ and $\Phi(g_0) \ne 0$ for some $g_0$ integral at the places over $p$, and some good prime lies under $w_0$. Suppose that $\xi_V^\vartheta$ has weight $\lambda$. Let $(r, W)$ be an auxiliary choice, $N$ a level with $r \mid N$ whose group consists of stable elements, and take a type at $w_0$: the group $K$ of $j(k')$ with $\vartheta(k')$ in the level of $V$ and components at $W$ in the Iwahori subgroup, the subgroup $K_N$, and the transpose inverse of $(J, \chi)$. Suppose that $j$ gives the local components at the places prime to $p$, and that $j(g)$ is regular whenever the components of $g$ at all places over some prime $q \ne p$ have separable characteristic polynomial. Then for all Hecke elements $g_j$ at level $N$ with numbers $\theta_j$ that are seen, there is an integral Hecke function $f$ at level $N$ such that $\theta$ is an eigensystem of weight $\lambda$ detected by $f$, for the family of functions of the $g_j$.

Lean: `UpperTheory.Gal.Spc.specData`.

*Proof.* Let $e$ be the function of the type at $1$; it is idempotent and lies in $\mathcal{H}(K_N)$. Since every smooth irreducible representation with a $\chi$-eigenvector of $J$ is cuspidal, $e$ is cuspidal for the splitting of $G$ at $w_0$. We take as given Hecke operators $u, u'$ with $e * u = u = u * e$ and $u' * u = e$, such that $u$ commutes with the functions of the type at elements trivial at $w_0$ and at $W$, and such that for each $m \ge 1$ the support of $u^{*m} * e$ consists of integral elements whose components at each $w \in W$ lie in a set $X_w$ of elements with separable characteristic polynomial, stable under the Iwahori subgroup. We also take as given that the functions of the $g_j$ lie in $\mathcal{H}(K_N)$, that each $g_j * e$ lies in the span on which $u$ commutes and the $g_j$ commute on $e$, and that $\theta$ has an eigenvector, namely the form of $V$ moved to a definite form by the frame. These facts give the Hecke relations for $(g, e, u, u')$.

For $m \ge 1$, let $A_m$ be the set of $y$ with components in $X_w$ for all $w \in W$. It contains the support of $u^{*m} * e$ and is stable under the supports of the $g_j$, whose components at $W$ lie in the Iwahori subgroup: the deck elements lie in $K_r$, and the sites lie over primes different from $r$. Each $y \in A_m$ is regular: its components at the places $w \in W$ are separable, hence so are those at $c(w)$, and these are all the places over $r$, so the regularity hypothesis applies with $q = r$. Theorem 3.15.2, with finitely many classes of definite forms and the weight hypothesis, gives $m \ge 1$ such that $\theta$ is detected by $f = u^{*m} * e$. This $f$ lies in $\mathcal{H}(K_N)$ and is supported on integral elements. $\square$

**Theorem 3.15.6 (choice of auxiliary prime).** Suppose that $\xi_V^\vartheta$ has weight $\lambda$ for every vector $V$. Let $n$, $S$, $F$, $V$ satisfy the first four hypotheses of Theorem 3.15.5. Then for every finite set $X$ of primes there is a prime $r_0 \notin X$ with $r_0 \ne p$ such that: for every level $N$ with $r_0 \mid N$ whose group consists of stable elements, and all seen pairs $(g_j, \theta_j)$, there is an integral Hecke function $f$ at level $N$ such that $\theta$ is an eigensystem of weight $\lambda$ detected by $f$.

Lean: `UpperTheory.Gal.Spc.specTopG`.

*Proof.* Take an auxiliary choice $(r, W)$ with $r \notin X$, and put $r_0 = r$. Given $N$, take the type at $w_0$ of Theorem 3.15.5. The frame gives the local components of $j$ at the places prime to $p$ and the regularity of $j(g)$ under separability at the places over a prime $q \ne p$. Apply [Theorem 3.15.5](/entry/spec-data/). $\square$

**Theorem 3.15.7 (spectral test functions exist).** The conclusion of Theorem 3.15.6 holds for every odd $n$, setup, frame and vector that satisfy its hypotheses.

Lean: `UpperTheory.Gal.Int.Geo.Pl.specTop_holds`.

*Proof.* This is [Theorem 3.15.6](/entry/spec-top-g/) applied to the fact that $\xi_V^\vartheta$ has the weight of $V$ for every vector $V$. $\square$

**Remark 3.15.8 (Formalization).** `specOfF` proves `SpecOfF` with `words`, `cuspIdeal`, `clsMove`, `opAlg`, `forms_fin`, `GlobalTheory.T.finite_doubleCoset_definiteHermitianForm_level`, `vanPairs`, `vanForms` and the linear-algebra lemma `specAlg`; we read `specOfF` and `specAlg`, whose projection and trace facts are `pProjOne_holds` and `pTracePow_holds`, but not the other helpers, so the Levi argument for goodness and the Newton argument are the standard ones and not read from the code. `TypeSlice.lean` also holds `SpecOf`, the same statement without the finiteness of classes. `specData` uses `tyTop`, `auxFn`, `memFn`, `memComm`, `eigEx`, `pTfIdem`, `pTfAdm`, `span_fix`, `splitC`, `cuspIrr_kFinite_rep_eq_centralCuspForm`, `sepConj` and `FinCls_holds`, which we did not open. The hypotheses `Odd n`, `Sc`, `Gen`, `Off` and the good prime under $w_0$ are not used in `specData` itself; they pass through to these helpers. `specTopG` takes $(r, W)$ from `auxiliary_prime_holds` and the type from `tyEx`; the statement it uses, `AuxiliaryInertOddPrime`, asks neither inertness nor oddness, and $W$ consists of split places. `SpecTopG` has the same text as `SpecTop`, so `specTop_holds` is `UpperTheory.Gal.Spc.specTopG wtOf_holds`, with `WtOf` the weight hypothesis.
