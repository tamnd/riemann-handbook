---
title: The integral connection and the Taylor formula
decls:
  - GlobalTheory.IntConnTaylor.main
  - GlobalTheory.T.integralConnection_taylorFormula_tameBreuilKisin
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The integral connection and the Taylor formula

Let $P$ be a $\varphi$-module over the Breuil-Kisin ring of a tame field that comes from a prismatic F-crystal. This section proves that the canonical connection of $P$ preserves the divided power lattice of $P$, and that the action of $G_{K_\varpi}$ on the Galois lattice is the Taylor series of this connection. The input is the theorem of Bhatt and Scholze on crystalline lattices, and the rings of [the crystalline prisms](/entry/exists-crys-prisms/). The result is used in the next section but one, to build the connection of a Breuil-Kisin pack for a good lattice.

We keep the notation of the previous section: a prime $\ell$, integers $a, e \ge 1$, a system of roots $\varpi$, the tame field $K_\varpi$, the Breuil-Kisin prism $\mathfrak{S} = W[[X]]$ with $E = X^e + \ell$, and the ring $\mathcal{S} \subseteq L[[X]]$ of series $\sum c_k X^k$ with $|c_k| \cdot |\lfloor k/e \rfloor !| \le 1$ and $c_k \lfloor k/e \rfloor ! \to 0$. Here $L$ is a finite extension of $\mathbb{Q}_\ell$ that contains $W[1/\ell]$, with ring of integers $\mathcal{O}$, and with tame descent data for $(L, \ell, e, a)$. For a finite set $\iota$, a *vector* is a family $v = (v_\tau)_{\tau \in \mathbb{Z}/a}$ with $v_\tau \in L[[X]]^\iota$.

**Definition 7.12.1 ($\varphi$-module).** Let $\mathfrak{S}_{\mathcal{O}} = \mathcal{O}[[X]]$. A *$\varphi$-module* $P$ of rank $\iota$ is a family of invertible matrices $Y_\tau \in \mathrm{GL}_\iota(\mathfrak{S}_{\mathcal{O}}[1/E])$, for $\tau \in \mathbb{Z}/a$. Its Frobenius is the map of vectors
$$\varphi(v)_\tau = Y_\tau\, \mathrm{frob}(v_{\tau - 1}),$$
where $\mathrm{frob}$ is $X \mapsto X^\ell$ on each entry. The *lattice* $M$ of $P$ is the set of vectors with entries in $\mathfrak{S}_{\mathcal{O}}$. The *divided power lattice* $\mathcal{M}$ of $P$ is the set of vectors $v$ such that, for each $\tau$, $v_\tau$ is an $\mathcal{S}$-linear combination of the columns of $Y_\tau$.

So the columns of $Y_\tau$ span the image of $\varphi$ on $M$ at the place $\tau$, and $\mathcal{M}$ is the $\mathcal{S}$-span of $\varphi(M)$. The ring $\mathcal{S}$ contains $E^k/k!$, so $\mathcal{M}$ is the module of $P$ over the divided power envelope of $(E)$.

**Definition 7.12.2 (Connection).** A *connection* on $P$ is an $L$-linear map $\nabla$ on vectors such that:

1. $\nabla(f v) = f' v + f \nabla v$ for every family $f = (f_\tau)$ of series in $L[[X]]$, where $f'$ is the derivative $d/dX$ entry by entry;
2. $\nabla(\mathcal{M}) \subseteq \mathcal{M}$.

Put $N = X \nabla$, and for $i \ge 0$ put $N_{(i)} = N(N - 1)\cdots(N - i + 1)$, with $N_{(0)} = 1$.

Each $\varphi$-module has a *canonical connection* $\nabla_P$: an $L$-linear map on vectors with the Leibniz rule 1. It is the conjugate of $d/dX$ by a matrix $\xi_\tau$ with constant term $1$ that is fixed by the Frobenius relation of $P$. We do not unfold it. The point of this section is condition 2: that $\nabla_P$ preserves $\mathcal{M}$.

Since $N$ preserves $\mathcal{M}$ when $\nabla$ does, so do all $N_{(i)}$. On $X^n$, $N_{(i)}$ acts by $n(n-1) \cdots (n - i + 1) = i! \binom{n}{i}$, so the series $\sum_i \gamma_i(x) N_{(i)}$ acts on $X^n$ by $(1 + x)^n$. This is why it is the Taylor series of the substitution $X \mapsto (1 + x) X$.

Now let $T$ be a $G_{\mathbb{Q}_\ell}$-stable $\mathcal{O}$-lattice in a finite-dimensional $L$-representation of $G_{\mathbb{Q}_\ell}$. Let $W_{\mathcal{O}}$ be the ring of Witt vectors of $\mathcal{O}_{C}^\flat$ with coefficients in $\mathcal{O}$, with Frobenius $\varphi$ (we do not unfold it). The Frobenius of $P$ extends to a semilinear map $\varphi_W$ of $W_{\mathcal{O}}^\iota$ through $X \mapsto [\varpi^\flat]$ and the embeddings $t_\tau$.

**Definition 7.12.3 (Identification).** An *identification* of $P$ with $T$ is a $W_{\mathcal{O}}$-linear isomorphism
$$j : W_{\mathcal{O}}^\iota \to W_{\mathcal{O}} \otimes_{\mathcal{O}} T$$
with $j \circ \varphi_W = (\varphi \otimes 1) \circ j$. The identification *comes from an F-crystal* if there are a prismatic F-crystal $\mathcal{E}$ over $\mathcal{O}_{K_\varpi}$ and a map $j_{\mathcal{E}}$ that realises the restriction of $T$ to $G_{K_\varpi}$ at the $A_{\inf}$-prism, such that the image of $\mathcal{E}(\mathfrak{S})$ under $j_{\mathcal{E}} \circ \mathcal{E}(i_\varpi)$, carried to $W_{\mathcal{O}} \otimes T$, is the image of $M$ under $j$.

The F-crystals and realisations are those of [Bhatt-Scholze integrality](/entry/bhatt-scholze-integral/). The fixed points of $\varphi \otimes 1$ in $W_{\mathcal{O}} \otimes T$ are $1 \otimes T$, so an identification gives a copy of $T$ inside $W_{\mathcal{O}}^\iota$, and $G_{K_\varpi}$ acts on it through $T$.

**Definition 7.12.4 (Taylor property).** Let $j$ be an identification of $P$ with $T$, and $\nabla$ a connection on $P$. Let $c$ be the comparison map from $\mathcal{M}$ to $(\mathcal{O} \otimes_{\mathbb{Z}_\ell} A_{\mathrm{cris}})^\iota$, and let $g$ act on $\mathcal{O} \otimes A_{\mathrm{cris}}$ through $A_{\mathrm{cris}}$. The pair $(j, \nabla)$ has the *Taylor property* if for each $g \in G_{K_\varpi}$ there is a matrix $\Gamma_g$ of $g$ on the lattice of $j$ with the following property. For each $m \in \mathcal{M}$ and $r \ge 0$ there is $n_0$ such that for all $n \ge n_0$,
$$\Gamma_g\, g\big(c(m)\big) - \sum_{i < n} \gamma_i(\mu(g))\, c\big(N_{(i)} m\big) \in \ell^r (\mathcal{O} \otimes A_{\mathrm{cris}})^\iota.$$

Here $\mu(g)$ and $\gamma_i$ are as in [the crystalline prisms](/entry/exists-crys-prisms/). In words: $g$ acts on $\mathcal{M}$, after the comparison with $A_{\mathrm{cris}}$, by the series $\sum_i \gamma_i(\mu(g)) N_{(i)}$, which converges $\ell$-adically. We do not unfold the comparison map $c$, nor the condition that $\Gamma_g$ is the matrix of $g$.

The input is the integral comparison of Bhatt and Scholze for lattices over a ring of integers $\mathcal{O}_L$.

**Theorem 7.12.5 (Bhatt-Scholze, crystalline lattices).** Let $\ell$ be a prime, $K$ a finite extension of $\mathbb{Q}_\ell$, and $(P_0, e)$ an $A_{\inf}$-prism over $\mathcal{O}_K$.

1. Let period data be given that are tied to Fontaine's rings. Let $L$ be a finite extension of $\mathbb{Q}_\ell$, and $T$ a $G_K$-stable $\mathcal{O}_L$-lattice in a crystalline $L$-representation of $G_K$. Then there is a prismatic F-crystal $\mathcal{E}$ over $\mathcal{O}_K$ with a map $j : \mathcal{E}(P_0) \to W(C^\flat) \otimes_{\mathbb{Z}_\ell} T$ that realises $T$, as a $\mathbb{Z}_\ell$-module with $G_K$-action, at $(P_0, e)$.
2. Let $(\mathcal{E}, j)$ and $(\mathcal{E}', j')$ realise $(T, \rho)$ and $(T', \rho')$ at $(P_0, e)$. For every $\mathbb{Z}_\ell$-linear $f : T \to T'$ with $f \circ \rho(g) = \rho'(g) \circ f$ for all $g$, there is a unique map $u : \mathcal{E} \to \mathcal{E}'$ of F-crystals with $j' \circ u_{P_0} = (1 \otimes f) \circ j$.

This is B. Bhatt and P. Scholze, "Prismatic F-crystals and crystalline Galois representations", *Cambridge J. Math.* 11 (2023), Theorem 1.2, for the lattice $T$ seen as a $\mathbb{Z}_\ell$-lattice. We take it as an input.

**Theorem 7.12.6 (Integral connection and Taylor formula).** Assume the theorem of Bhatt and Scholze on crystalline lattices. Let $\ell \ne 2$ be a prime, $a, e \ge 1$, $\varpi$ a system of roots, and $L$ a finite extension of $\mathbb{Q}_\ell$ that contains $W[1/\ell]$, with tame descent data for $(L, \ell, e, a)$. Let $P$ be a $\varphi$-module of rank $\iota$ over $\mathcal{O}$, $T$ an $\mathcal{O}$-lattice of $G_{\mathbb{Q}_\ell}$, and $j$ an identification of $P$ with $T$ whose restriction to $G_{K_\varpi}$ comes from an F-crystal. Then the canonical connection $\nabla_P$ is a connection on $P$, that is, $\nabla_P(\mathcal{M}) \subseteq \mathcal{M}$, and $(j, \nabla_P)$ has the Taylor property.

Lean: `GlobalTheory.IntConnTaylor.main` (also `GlobalTheory.T.integralConnection_taylorFormula_tameBreuilKisin`, a second name).

*Proof.* *Step 1: the two-variable rings.* There are a ring map $\mathrm{sh} : L[[X]] \to L[[X]][[Y]]$ with $i!\,[Y^i]\,\mathrm{sh}(f) = f^{(i)}$, that is, $\mathrm{sh}(f)(X, Y) = f(X + Y)$, and a ring endomorphism $\varphi_2$ of $L[[X]][[Y]]$ with $\varphi_2(f) = \mathrm{frob}(f)$ and $\varphi_2(\mathrm{sh} f) = \mathrm{sh}(\mathrm{frob} f)$ for $f \in L[[X]]$. These are the data of [the crystalline prisms](/entry/exists-crys-prisms/).

*Step 2: an integral stratification.* The F-crystal $\mathcal{E}$ has a value on the prism $P$ of the previous section, and the two maps $p_0$ and $p_1$ give two base changes of $\mathcal{E}(\mathfrak{S})$ to $P$, which $\mathcal{E}$ identifies. With the theorem of Bhatt and Scholze, the matrix of this identification, carried by the maps $j_\tau$ into $L[[X]][[Y]]$, gives a family of matrices $\varepsilon_\tau$ over $L[[X]][[Y]]$ with three properties: $\varepsilon_\tau = 1$ at $Y = 0$; a Frobenius relation that links $\varepsilon_\tau$, $\varphi_2(\varepsilon_{\tau - 1})$ and the matrices $Y_\tau$; and $k!\,[Y^k]\,\varepsilon_\tau$ has entries in $\mathcal{S}$ for every $k$. This step uses $\ell \ne 2$ and the hypothesis that $j$ comes from an F-crystal.

*Step 3: the coefficients of the stratification.* For a family $\varepsilon_\tau$ with the first two properties, the coefficients are given by the canonical connection: for each $n$, $n!\,[Y^n]\,\varepsilon_\tau$ is the matrix of the coordinates of the vectors $\nabla_P^n\, \varphi(e_k)$, $k \in \iota$, in the columns of $Y_\tau$. Here $e_k$ is the $k$-th standard basis vector. By the third property of Step 2, $\nabla_P^n\, \varphi(e_k) \in \mathcal{M}$ for all $n$ and $k$.

*Step 4: $\nabla_P$ preserves $\mathcal{M}$.* The vectors $\varphi(e_k)$ lie in $\mathcal{M}$ and generate it over $\mathcal{S}$, and $\nabla_P\, \varphi(e_k) \in \mathcal{M}$ by Step 3. For $m = \sum_k f_k\, \varphi(e_k)$ with $f_k$ in $\mathcal{S}$, the Leibniz rule gives $\nabla_P m = \sum_k \big(f_k'\, \varphi(e_k) + f_k\, \nabla_P \varphi(e_k)\big)$. The ring $\mathcal{S}$ is stable under $d/dX$, so $\nabla_P m \in \mathcal{M}$. So $\nabla_P$ is a connection on $P$.

*Step 5: the Taylor property.* By Step 3, $X^k$ times the coordinates of $\nabla_P^k\, \varphi(e_j)$ in the columns of $Y_\tau$ lie in $\mathcal{S}$, since $X \in \mathcal{S}$. These are the conditions on the coefficients in part 5 of [the crystalline prisms](/entry/exists-crys-prisms/). With them, the evaluation maps of part 6 of that theorem, applied to the stratification, write the matrix $\Gamma_g$ of $g$ on the Frobenius basis as an $\ell$-adically convergent divided power series in $\mu(g)$ with coefficients $X^k \nabla_P^k$. This uses the theorem of Bhatt and Scholze a second time, to identify the matrix of $g$ with the evaluation of the stratification. Finally, $X^k \frac{d^k}{dX^k} = N_{(k)}$ for the operator $N = X \frac{d}{dX}$, and the same identity holds for $\nabla_P$, since $\nabla_P$ is the conjugate of $d/dX$. This turns the series into the Taylor property. $\square$

**Remark 7.12.7 (Formalization).** The conclusion reads "there is a connection $C$ with $C.\nabla = \nabla_P$ and the Taylor property". So no new connection is built: $C$ is $\nabla_P$ together with the proof of Step 4 ([IntegralConnectionTaylorFormulaTameBreuilKisin.lean](lean:Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IntegralConnectionTaylorFormulaTameBreuilKisin.lean#L32)). Steps 1, 2, 3 and 5 are lemmas imported from "Statement" files (`exists_taylorShift_frobenius_twoVariable_compatible`, `exists_integral_crystal_stratification_matrix`, `frobeniusStratification_coeff_eq_connection_pow`, `galois_dividedTaylor_expansion_frobeniusBasis` and `galois_taylor_formula_breuilKisin_lattice`); we read their uses but not their proofs, so the descriptions of Steps 2, 3 and 5 follow their names and the way the proof applies them. Step 4 is `nabla_mem_MM_of_basis`. The theorem of Bhatt and Scholze is a hypothesis, used only in Steps 2 and 5. We did not unfold the canonical connection (`PhiMod.nabla`), the comparison map `toCris`, the matrix condition `IsLMat` or the ring `OW`. The second name is a one-line wrapper.
