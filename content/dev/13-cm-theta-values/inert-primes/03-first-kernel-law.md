---
title: The first kernel law
decls:
  - Formalism.L2.KerInert.KGLt.first_kernel_small_of_frame
  - Formalism.L2.KerInert.KGLt.first_kernel_small_of_frame_twist
  - Formalism.L2.KerInert.KGLt.first_kernel_law_global_small
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The first kernel law

This section attaches a family of power series to a formal group system at an inert prime $p \ge 5$: one series for each level $j$ and each pair of lattice tuples at the levels $j$ and $j + 1$, built from a theta kernel of the pair of lattices. The main theorem says that, read through any frame, each series factors as the exponential of a quadratic expression in the pairing series of Section 1 times an integral series. This is the *first kernel law*. From it we deduce three of the admissibility conditions of the pending tuple of the system. The inputs are [the laws of the pairing series](/entry/be-winert-of-a/) and [the integrality of theta kernels](/entry/kernels-integral-inert/). The result feeds [the admissibility theorem](/entry/admissible-general-of-kernel-law/) of Section 4.

### Formal group systems and the generator condition

We use formal group systems as in [the chapter on elliptic torsion](/entry/pending-tuple-admissible/). A formal group system $X$ at $p$ has levels $j = 0, 1, \dots$ below a top level $m$, a finite set of places $v$, at each level a set of lattice tuples, and frames between tuples at consecutive levels. At each level the tuples fall into finitely many classes, and we fix a set of *representatives*. A *pending tuple* of $X$ attaches to each level $j$, each pair $(L_a, L_a')$ of tuples at the levels $j$ and $j + 1$, and each frame $\varphi$, a series $\Theta_A(\varphi)$, read from a family of series through the frame; it also carries a pairing series $\beta$ in two variables.

Let $W = W(\overline{\mathbb{F}}_p)$ be the Witt vectors, the ring of integers of the completion of the maximal unramified extension, with fraction field $K_0$ and Frobenius $\sigma$. For series $f, g$ over $K_0$ we write $f \simeq g$ if $f - g$ has constant term $0$ and the exponential of $f - g$, after the formal logarithm is substituted into the parameters, equals $1 + h$ with $h$ a series over $W$ with constant term $0$. A series $\beta(X, Y)$ has the *pairing property* if:
1. every monomial of $\beta$ has degree at least $1$ in each variable;
2. $\beta(X_0 + X_1, X_2) - \beta(X_0, X_2) - \beta(X_1, X_2) \simeq 0$ and $\beta(X_0, X_1 + X_2) - \beta(X_0, X_1) - \beta(X_0, X_2) \simeq 0$;
3. $\beta(\alpha X_0, X_1) \simeq \beta(X_0, \sigma(\alpha) X_1)$ for every $\alpha \in W$ with $\sigma^2\alpha = \alpha$.

**Definition 6.3.1 (Extension generator condition).** Let $\beta$ be a series in two variables. A series $\Theta$ in variables indexed by a set $I \sqcup I$ satisfies the *extension generator condition* for $\beta$ if there are series $\Phi$ and $U$ such that:
1. $\Theta = \exp(-\Phi)\cdot U$;
2. $U$ is integral after the substitution of the formal logarithm into the parameters;
3. $\Phi(-X) \simeq \Phi(X)$;
4. $\beta$ has the pairing property;
5. $\Phi \simeq \sum_{e \in I} \beta(X_{e}, X_{e}')$, where $X_e$ and $X_e'$ are the two variables of index $e$.

So $\Theta$ is, up to an integral unit, the exponential of minus a sum of pairings. This is the shape of a theta function of a polarized formal group: the quadratic part of its logarithm comes from the biextension, and the rest is integral.

**Definition 6.3.2 (First kernel law).** A family $F$ of series $F_j(L_a, L_a')$ satisfies the *first kernel law* for $\beta$ if, for every $j < m$, every representative $L_0$ at level $j$, every lattice tuple $L_a'$ at level $j + 1$ and every frame $\varphi$ from $L_0$ to $L_a'$, the series read from $F_j(L_0, L_a')$ through $\varphi$ satisfies the extension generator condition for $\beta$.

### The kernel family

Fix data $(\mathfrak{c}, \delta, g)$ at $(K, p)$ as in Section 1, with $p \ge 5$ inert and the curve over $W$, theta data $B$ on the same lattice, and a character $\chi$ as in Section 2. Let $c$ be the scale of a Lubin-Tate isomorphism for the formal group of $g$; the pairing series $\beta$ of the pending tuple is the pairing series of $g$ in Lubin-Tate coordinates. Fix frame data: for each level $j$ and tuple $L_a$, a lattice $\Lambda_j(L_a)$ over $\mathcal{O}_E$, a translation and a frame matrix. Fix a finite set $S$ of primes of $E$, an integer $c_l$, a family of values $\Xi_0(j, L_a, L_a', y)$, a family of idelic scalars $\mu_T$, a bijection between the pairs $(v, s)$ of places and positions and the embeddings $\mathrm{Tau}$, and maps $\rho_v$ from $E$ to the local fields of the places.

The *kernel family* attaches to $(j, L_a, L_a')$ the series
$$\begin{aligned} F_j(L_a, L_a') = \; & \text{linear substitution by } c \cdot (\text{frame matrix}) \text{ of} \\ & p^{e_j}\,\lambda\bigl(s_j \cdot \Theta_\chi(\Lambda_j(L_a), \Lambda_{j+1}(L_a'); \Xi)\bigr), \end{aligned}$$
where $\Theta_\chi(\Lambda, \Lambda'; \Xi)$ is the theta kernel of the pair at level $c_l$ with coefficients $\Xi$ (the values $\Xi_0$ moved by the translations), $s_j$ is the product of the scalars $\mu_T$ at the two levels with powers of $\chi$ at the determinants of the two lattices, and $e_j = \sum_v m_v(j+1)\,(\ell_v(j + 1) - \ell_v(j))$ is a sum of differences of lengths.

We use the following hypotheses, for every $j < m$, every representative $L_0$ at level $j$ and every lattice tuple $L_a'$ at level $j + 1$.
- (A) The pair $(\Lambda_j(L_0), \Lambda_{j+1}(L_a'))$ is admitted.
- (C) $c_l > 0$ and $p \nmid c_l$.
- (X) There is a finite set $S_0$ of primes with $p \notin S_0$ such that every value $\Xi_0(j, L_0, L_a', y)$ is algebraic and $|\lambda'(\cdot)| \le 1$ for every prime $q \notin S_0$ and every ring map $\lambda' : \overline{\mathbb{Q}} \to \mathbb{C}_q$.
- (S) The scalar $s_j$ is algebraic and $|p^{e_j}\lambda(s_j)| \le 1$.
- (P) The embeddings match the places: $\lambda\tau_{(v,s)}(x) = \rho_v(x)$ or $\rho_v(\bar x)$, after a fixed twist, according to the parity of $s$.
- (M) The frame matrices are invertible.
- (F) For every orthonormal local basis $b$ of $Y(\Lambda_j(L_0), \Lambda_{j+1}(L_a'))$ and every frame, the images $\rho_v(b_i)$ map the columns of the frame into the expected column spans.

We write (X') for the weaker form of (X) that asks the condition only for $j < m$, representatives $L_0$ and lattice tuples $L_a'$, and (X'') for the stronger form that asks it for all $j$ and all tuples.

**Theorem 6.3.3 (First kernel law, strong form).** Assume the theorem on good models, the data and hypotheses above with (X'') in place of (X). Then the kernel family satisfies the first kernel law for the pairing series of $g$ in Lubin-Tate coordinates.

Lean: `Formalism.L2.KerInert.KGLt.first_kernel_small_of_frame`

*Proof.* Fix $j < m$, a representative $L_0$ and a lattice tuple $L_a'$. Put $\Lambda = \Lambda_j(L_0)$ and $\Lambda' = \Lambda_{j+1}(L_a')$. The kernel series is $p^{e_j}\lambda(s_j\,\Theta_\chi)$, and the family is a linear substitution of it. We check the inputs of a dictionary that turns the integrality of kernels into the first kernel law. First, the kernel series is a combination of translates for $(\Lambda, \Lambda')$ in the sense of Section 2. The values of the moved coefficients are algebraic and integral at $p$ by (X''); the level $c_l$ is prime to $p$ by (C); the pair is admitted by (A); and the scalar keeps integrality by (S). Second, an orthonormal local basis of $Y(\Lambda, \Lambda')$ exists: the global orthonormal basis for four copies gives one, with weak approximation and separation of the primes above $p$. Third, the traces of $\lambda$ over the embeddings match the rank conditions of the frame, by the sum formula for traces of $\tau$. Fourth, the frame hypotheses follow from (F), with the Frobenius twist and the integrality of the twists. Fifth, the pairing series has the pairing property: this is [the theorem on algebraicity](/entry/be-winert-of-a/) of Section 1 with its four inputs proved, converted to the pairing property in Lubin-Tate coordinates. With these inputs and [the integrality at an inert prime](/entry/kernels-integral-inert/), the dictionary gives the extension generator condition for every frame from $L_0$ to $L_a'$. $\square$

**Theorem 6.3.4 (First kernel law).** Assume the theorem on good models and the data and hypotheses above, with (X') in place of (X). Then the kernel family satisfies the first kernel law for the pairing series of $g$ in Lubin-Tate coordinates.

Lean: `Formalism.L2.KerInert.KGLt.first_kernel_small_of_frame_twist`

*Proof.* Define $\Xi_1(j, L_a, L_a', y) = \Xi_0(j, L_a, L_a', y)$ if $j < m$, $L_a$ is a representative and $L_a'$ is a lattice tuple, and $\Xi_1 = 0$ otherwise. Then $\Xi_1$ satisfies (X''): on the given tuples this is (X'), and $0$ is algebraic and integral everywhere. The kernel family for $\Xi_1$ agrees with the kernel family for $\Xi_0$ at every $j < m$, representative $L_0$ and lattice tuple $L_a'$, and the first kernel law only looks at these. So [the strong form](/entry/first-kernel-small-of-frame/) for $\Xi_1$ gives the claim for $\Xi_0$. $\square$

### Three admissibility conditions

The pending tuple built from the kernel family has three conditions that come from the first kernel law. Condition (2) asks an extension condition at each place $v$. Condition (2b) asks the extension generator condition for all $j < m$, all lattice tuples at level $j$ (not only representatives), all lattice tuples at level $j + 1$ and all frames. Condition (3) asks that, after the differential operators of the system are applied and the result is restricted to zero, the coefficients have valuation at least $0$.

**Theorem 6.3.5 (Translates of the inert kernel at a place).** Assume the theorem on good models. Let $p \ge 5$ be inert, let the data be as above with $\lambda$ equal to the ring map of $g$, and assume (A), (C), (X'), (S), (P), (M) and (F). Then the pending tuple built from the kernel family satisfies conditions (2), (2b) and (3).

Lean: `Formalism.L2.KerInert.KGLt.first_kernel_law_global_small`

*Proof.* [The first kernel law](/entry/first-kernel-small-of-frame-twist/) holds for the kernel family. Each lattice tuple at level $j$ is equivalent to a representative, and the series and frames move along the equivalence. So condition (2b) is equivalent to the first kernel law on representatives, and it holds. Condition (2) follows from (2b), since the local extension condition at $v$ is a variant of the generator condition read at $v$. Condition (3) follows from (2b) together with condition (11) at an inert prime, which holds for the data at $(K, p)$ over $W$. Condition (11) says: for each place $v$ and each $j < m$, and for every series $U$ that is integral in the parameters, the operators of the system at $v$, applied to $\exp(-\Phi_{j,v})\,U$ and restricted to zero, give coefficients of valuation at least $0$; here $\Phi_{j,v}$ is the quadratic series of the pending tuple at $v$. By (2b), every $\Theta_A(\varphi)$ has the form $\exp(-\Phi)\,U$ with $U$ integral, so condition (11) bounds its coefficients. $\square$

**Remark 6.3.6 (Formalization).** The three theorems sit under `variable [Fact CM2] in` ([FirstKernelSmallOfFrameTwist.lean](lean:Formalism/LocalToGlobal/InertKernelTheory/InertCoprimeLemmas/FirstKernelSmallOfFrameTwist.lean#L18), lines 18, 85 and 122). The names "global" and "small" in `first_kernel_law_global_small` do not describe the statement, which is local at one place and one prime. The twisted form exists only because the hypothesis on $\Xi_0$ in the strong form is stated for all levels and all tuples, while the main theorem has it only on representatives. In the strong form the inertness hypothesis is passed twice to the dictionary `K1_representatives_LT_of_dictionary` (near line 80). The pairing property comes through `beProp_ofA inert_facts_first_hold`. The frame hypotheses (P), (F) and the Lubin-Tate isomorphism are not unfolded beyond what the text says.
