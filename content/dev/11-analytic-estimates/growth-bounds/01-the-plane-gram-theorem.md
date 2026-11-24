---
title: The plane Gram theorem
decls:
  - Formalism.MainNotions.PlaneGram.plane_gram_theorem_of_five_lemmas
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The plane Gram theorem

This section proves a lift bound for polynomials in several groups of $r$ variables over a $p$-adic field. A polynomial $F$ of norm $1$ with valuation conditions along one-parameter tori is paired with a polynomial built from it, and the theorem bounds the valuation of the pairing from above. The proof combines five properties: a valuation calculus, a spanning family, a projector, a digit splitting of factorials and a congruence for derivatives. The next section transfers it to discrete valuation rings, in the form that the second theorem uses. The Background on [discrete valuation rings](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices) and [divided powers](/learn/combinatorics/#binomial-coefficients-factorials-and-divided-powers) has the basic facts.

### Polynomials and the Fock pairing

Let $K$ be a field of characteristic $0$ and let $v : K \to \mathbb{Q} \cup \{\infty\}$ be an additive valuation. Let $\mathcal{O} = \{x : v(x) \geq 0\}$. Let $p$ be a prime number.

**Definition 5.1.1 (Valuation hypothesis).** We say that $(K, v, p)$ satisfies the *valuation hypothesis* if $p \geq 5$ and $v(p) = 1$.

Let $L$ be a finite set of *letters* and let $r \geq 1$. For each letter $i$ and each $a \in \{1, \dots, r\}$ we take a variable $X_{i,a}$. An exponent is a function $\alpha : L \times \{1, \dots, r\} \to \mathbb{N}$, and $X^\alpha = \prod X_{i,a}^{\alpha(i,a)}$. Put $\alpha! = \prod_{x}\alpha(x)!$.

**Definition 5.1.2 (Multihomogeneous polynomials).** Let $d : L \to \mathbb{N}$. Then $\mathrm{Pol}_K(r, d)$ is the $K$-span of the monomials $X^\alpha$ with $\sum_a \alpha(i,a) = d_i$ for every letter $i$. The set $\mathrm{Pol}_{\mathcal{O}}(r, d)$ consists of the elements of $\mathrm{Pol}_K(r, d)$ with all coefficients in $\mathcal{O}$.

**Definition 5.1.3 (Fock pairing and Fock valuation).** For polynomials $F = \sum F_\alpha X^\alpha$ and $G = \sum G_\alpha X^\alpha$ put
$$\langle F, G\rangle = \sum_{\alpha} F_\alpha\, G_\alpha\, \alpha!.$$
The *Fock valuation* of $F$ is
$$v_{\mathrm{BB}}(F) = \min_{F_\alpha \neq 0}\Big(v(F_\alpha) + \tfrac{1}{2}v(\alpha!)\Big).$$

This is the Fock (or Bombieri) pairing without conjugation. Each term of the sum has valuation $v(F_\alpha) + v(G_\alpha) + v(\alpha!)$, so $v(\langle F, G\rangle) \geq v_{\mathrm{BB}}(F) + v_{\mathrm{BB}}(G)$.

For $d$ as above put $\lambda(n) = \log_p(n + r) + 1$ and
$$\kappa(d) = \sum_{i \in L} r\,\lambda(d_i).$$
This is the loss that appears when we pass between the integral structure and the Fock valuation.

### Valuations along a torus

Fix a sign for each letter: a letter is a *vector letter* or a *covector letter*. Let $g$ be the generic matrix in $\mathrm{GL}_r$, that is, the matrix of coordinates over the field of rational functions in its entries. Let $T$ be a further variable. Put
$$h = \big(g\,\mathrm{diag}(1, \dots, 1, T)\,g^{-1}\big)^{t}, \qquad h' = g\,\mathrm{diag}(1, \dots, 1, T^{-1})\,g^{-1}.$$

**Definition 5.1.4 (Torus valuation).** Let $S \subseteq L$. The substitution $\sigma_S$ fixes $X_{i,a}$ for $i \notin S$. For $i \in S$ it sends $X_{i,a}$ to $\sum_b h_{ab}X_{i,b}$ if $i$ is a vector letter, and to $\sum_b h'_{ab}X_{i,b}$ if $i$ is a covector letter. For a polynomial $F$, the coefficients of $\sigma_S F$ are Laurent polynomials in $T$. The *torus valuation* $\mathrm{val}_S(F)$ is the least order in $T$ of these coefficients. For a real number $\theta$ put
$$A_S(\theta) = \{F : \mathrm{val}_S(F) \geq \theta\}.$$

**Example 5.1.5.** Let $r = 1$. Then $h = T$ and $h' = T^{-1}$. The substitution sends $X_i$ to $TX_i$ for a vector letter $i \in S$ and to $T^{-1}X_i$ for a covector letter $i \in S$. So a monomial $X^\alpha$ has torus valuation $\sum_{i \in S,\ \text{vector}}\alpha_i - \sum_{i \in S,\ \text{covector}}\alpha_i$. For $r > 1$ the torus is a generic conjugate of the torus $\mathrm{diag}(1, \dots, 1, T)$, and the torus valuation measures the weight of $F$ along the last direction of a generic flag.

### The five properties

The proof takes five properties of these objects as input. We state them as definitions. The first four are properties of $K$ or of $(K, v, p)$ alone. In each statement $d$ is a degree vector and $F \in \mathrm{Pol}_K(r, d)$.

**Definition 5.1.6 (Property V2).** The torus valuations satisfy the following four rules.

1. $\mathrm{val}_S(X_{i,a}) \geq 0$ if $i$ is a vector letter, and $\mathrm{val}_S(X_{i,a}) \geq -1$ if $i$ is a covector letter.
2. Let $\partial^{(\beta)}$ be the divided derivative of order $\beta$ in the variables of one letter $i$, which sends $X^\alpha$ to $\prod_x\binom{\alpha_x}{\beta_x}X^{\alpha - \beta}$. Then $\mathrm{val}_S(\partial^{(\beta)}F) \geq \mathrm{val}_S(F) - |\beta|$ if $i$ is a vector letter, and $\mathrm{val}_S(\partial^{(\beta)}F) \geq \mathrm{val}_S(F)$ if $i$ is a covector letter.
3. If $S \subseteq S'$ and all letters of $S' \setminus S$ are vector letters, then $\mathrm{val}_S(F) \leq \mathrm{val}_{S'}(F)$.
4. If $S' \subseteq S$ and all letters of $S \setminus S'$ are vector letters, then $\mathrm{val}_S(F) - \sum_{i \in S \setminus S'}d_i \leq \mathrm{val}_{S'}(F)$.

**Definition 5.1.7 (Property SPAN).** Assume the valuation hypothesis. For every number of letters, every $r$, every choice of signs and every $d$ there is a finite family $(\Psi_b)$ in $\mathrm{Pol}_{\mathcal{O}}(r, d)$ with these properties. The family is linearly independent and spans $\mathrm{Pol}_{\mathcal{O}}(r, d)$ over $\mathcal{O}$. Each $\Psi_b$ is a product of column polynomials, each linear in the letters of one column, and each letter $i$ occurs $d_i$ times. Each $b$ carries a Pieri path, and if $F \in \mathrm{Pol}_{\mathcal{O}}(r, d)$ lies in $A_{S_i}(\theta_i)$ for the initial segments $S_i$ of the letters, then $F = \sum c_b\Psi_b$ with $c_b \in \mathcal{O}$, and $c_b \neq 0$ implies that the $i$-th height of the path of $b$ is at least $\theta_i$.

The heights of a path are sums of column values, $+1$ for a column of positive index and full height $r$, $-1$ for a column of index at most $0$ and height less than $r$, and $0$ otherwise. Compare [the Pieri rule](/learn/combinatorics/#the-pieri-and-littlewood-richardson-rules).

**Definition 5.1.8 (Fock projector).** Let $W$ be a set of polynomials. A *Fock projector* onto $W$ in degree $d$ is a map $\pi$ with $\pi F \in \mathrm{Pol}_K(r, d) \cap W$, $\pi F = F$ for $F \in W$, and $\langle F - \pi F, G\rangle = 0$ for all $G \in \mathrm{Pol}_K(r, d) \cap W$.

**Definition 5.1.9 (Property PROJ).** For every $S$ and $\theta$ a Fock projector $\pi_S$ onto $A_S(\theta)$ exists. Every such projector commutes with the Euler operators $X_{i,a}\partial_{i,a}$ for vector letters $i \notin S$. Two such projectors for $S$ and $S'$ commute if $S \subseteq S'$ or if $S$ and $S'$ are disjoint. Every such projector satisfies
$$v_{\mathrm{BB}}(F) \leq v_{\mathrm{BB}}(\pi_S F) + r^2\lambda\Big(2\sum_i d_i\Big).$$

**Definition 5.1.10 (Property DIG).** Let $g \geq 0$ and $q = p^g$. For each $\rho \in \{0, \dots, q - 1\}^r$ there are constants $c(\rho, n) \neq 0$ and units $\gamma(\rho, \beta)$ with
$$\prod_a(\rho_a + q\beta_a)! = c\Big(\rho, \sum_a\beta_a\Big)\prod_a\beta_a!\;\gamma(\rho, \beta).$$
For each integer $c \geq 1$ and $\varepsilon = \pm 1$, the product of these units over several twisted letters, raised to the power $\varepsilon$, agrees modulo valuation $c$ with a function $\beta \mapsto \sum_{m}\lambda_m\prod_x\binom{\beta_x}{m_x}$, with $\lambda_m \in \mathcal{O}$ and $\sum_x m_x \leq 6c$.

**Definition 5.1.11 (Property DER).** Let $q = p^g$ and $c \geq 1$. For a multi-index $M$ the divided derivative $\partial^{(M)}X^{\rho + q\beta}$ agrees modulo valuation $c$ with a sum
$$\sum_t c_t\,X^{\rho'_t}\,\Phi_q\big(X^{\delta_t}\,\partial^{(\kappa_t)}X^\beta\big),$$
where $\Phi_q$ replaces each variable by its $q$-th power, $c_t \in \mathcal{O}$ and $|\kappa_t| \leq |M|/q + c$.

So a divided derivative of order $|M|$ acts on the high digits as a derivative of order about $|M|/q$.

### Twist data and the lift bound

The lift bound concerns polynomials in two sets of letters. *Base letters* $b$ have degree $d^B_b$ and lie in one of $J$ segments. *Twisted letters* are pairs $t = (j, m)$ with $j < J$ and $m < r$; each has a degree $d^T_t$ and an exponent $g_t$, and we put $P_t = p^{g_t}$. For each segment $j$ there are chains of letters with thresholds $\theta_{j,i}$ and slopes $s_{j,i}$, link thresholds $\vartheta_{j,m} > 0$, an integer $c \geq 1$, and a unit function $\gamma$ on exponents. We call all of this *twist data*.

The polynomial $F$ lives on the old letters: base letters and twisted letters, with degree vector $d_O$. The lift lives on model letters: each base letter $b$, and three copies $\ell_t$, $w_t$ and $\tau_t$ of each twisted letter $t$. The map $\phi$ from model polynomials to old polynomials is the substitution
$$X_b \mapsto X_b, \quad X_{\ell_t} \mapsto X_t, \quad X_{w_t} \mapsto X_t^{P_t}, \quad X_{\tau_t} \mapsto X_t.$$
So $\ell_t$ carries the low digits of an exponent and $w_t$ the high digits. Put $n_0 = \frac{1}{2}v\big(\prod_i d_{O,i}!\big)$ and $\kappa = \kappa(d_O)$.

The conditions on $F$ are as follows. We say $F$ is *admissible input* if $F \in \mathrm{Pol}_K(r, d_O)$, if for every digit pattern $\rho$ the digit part of $F$ (the monomials with exponents $\equiv \rho$ modulo $P_t$, rewritten with the high digits on the letters $w_t$) has torus valuation at least $\theta_{j,i}$ on each chain set, and if $\mathrm{val}_{T(j,m)}(F) \geq \vartheta_{j,m}$ for $m + 2 \leq r$. Here $T(j,m)$ is the set of base letters of segment $j$ and the twisted letters $(j, m')$ with $m' > m$.

The output conditions on a model polynomial $G$ with constants $k_6$ and $k_{18}$ are: $G$ is integral; no letter $\tau_{(j,0)}$ occurs; the torus valuation on each chain set is at least $\theta_{j,i} - s_{j,i} - k_6c$; and the torus valuation on the set $Y(j,m)$ of $w$ letters, base letters and letters $\tau_{(j,m')}$ with $m' > m$ is at least $\vartheta_{j,m} - k_{18}c$. Low label exponents means that all exponents of the letters $\ell_t$ are less than $P_t$. Degree bookkeeping means that $\phi$ maps each monomial into $\mathrm{Pol}_K(r, d_O)$. Finally $\gamma\cdot H$ multiplies the coefficient of $X^\alpha$ in $H$ by $\gamma(\alpha)$.

The constants are as follows. Put $e = r^2\lambda(2\sum_i d_{O,i})$, $D_m = e\sum_j n_j$, where $n_j$ is the number of chains of segment $j$, and $D_l = J(r - 1)e$. The *size hypothesis* is
$$4(D_m + D_l + 3\kappa) < c,$$
and the *slope hypothesis with constant $k_H$* is $r\,d_j/P_{(j,m)} + k_H\,r\,c \leq s_{j',i}$ for the next segment $j'$. Put $E = D_m + D_l + 2\kappa$.

**Definition 5.1.12 (Uniform lift bound).** The *uniform lift bound* for $(K, v, p)$ says: assume the valuation hypothesis, let the twist data be valid (that is, $r, J > 0$, $c \geq 1$, the chains lie in their segments and increase strictly, $\vartheta > 0$, and $\gamma$ satisfies the digit approximation of Property DIG), and assume the slope hypothesis with $k_H = 13$ and the size hypothesis. Let $F$ be admissible input with $v_{\mathrm{BB}}(F) = 0$. Then there are model polynomials $G'$ and $R$ such that:

1. $G'$ satisfies the output conditions with $k_6 = 12$ and $k_{18} = 30$, and has low label exponents;
2. $R$ has no letter $\tau_{(j,0)}$, has low label exponents, and $v(R_\alpha) \geq c - E$ for all $\alpha$;
3. $G'$ and $R$ satisfy the degree bookkeeping;
4. $v_{\mathrm{BB}}\big(\phi(G' + R)\big) \geq n_0 - \kappa$;
5. $v\big(\langle F, \gamma\cdot\phi(G' + R)\rangle\big) - n_0 + \kappa \leq E + 2\kappa$.

Since $v_{\mathrm{BB}}(F) = 0$, clauses 4 and 5 place the valuation of the pairing between $n_0 - \kappa$ and $n_0 + \kappa + E$, a window that does not grow with $c$. In particular the pairing is not zero.

### The theorem

**Theorem 5.1.13 (Plane Gram theorem from five properties).** Let $K$ be a field of characteristic $0$ with an additive valuation $v$, let $p$ be a prime and let $C_0 \geq 1$. Assume Properties V2, SPAN, PROJ, DIG and DER. Then the uniform lift bound holds for $(K, v, p)$.

Lean: `Formalism.MainNotions.PlaneGram.plane_gram_theorem_of_five_lemmas`.

*Proof.* The proof has two stages and a final estimate.

The first stage produces a model polynomial $Z$. Properties V2 and PROJ give an integral $\tilde G \in \mathrm{Pol}_{\mathcal{O}}(r, d_O)$ with $\mathrm{val}_{T(j,m)}(\tilde G) \geq \vartheta_{j,m} - 6c$ for $m + 2 \leq r$ and $v(\langle F, \gamma\cdot\tilde G\rangle) \leq n_0 + D_l + 1$. Then Property V2 and Property SPAN lift $\tilde G$ to an integral model polynomial $Z$ with $\phi(Z) = \tilde G$, with low label exponents, no letter $\tau_{(j,0)}$, the degree bookkeeping, and torus valuation at least $\vartheta_{j,m} - 6c$ on each $Y(j,m)$.

The second stage corrects $Z$ on the chain sets. Properties DIG, V2, PROJ and DER, with the slope hypothesis for $k_H = 13$, give a linear map $\Omega$ on model polynomials and an integer $N_2 \leq D_m + \kappa/2 + 1$ such that, for every $Z$ as above:

1. $p^{N_2}\Omega(Z)$ is integral, and $\Omega(Z)$ keeps the label, degree and $\tau$ conditions;
2. $\Omega(Z)$ has torus valuation at least $\theta_{j,i} - s_{j,i} - 12c$ on each chain set;
3. if $Z$ has torus valuation at least $\theta$ on $Y(j,m)$, then $\Omega(Z)$ has torus valuation at least $\theta - 24c$ there;
4. $v\big(\langle F, \gamma\cdot\phi(\Omega Z)\rangle - \langle F, \gamma\cdot\phi(Z)\rangle\big) \geq c + n_0 - 2\kappa - D_m$.

Property DIG approximates the unit $\gamma$ by a polynomial in binomial coefficients of degree at most $6c$, and Property DER controls divided derivatives of digit monomials.

Now put $G' = p^{N_2}\Omega(Z)$ and $R = 0$. Clauses 1 to 3 of the lift bound follow from the list above: the chain bound holds with $k_6 = 12$, and the bound on $Y(j,m)$ holds with $\vartheta_{j,m} - 6c - 24c$, so with $k_{18} = 30$. For clause 4, $\phi(G')$ is integral and lies in $\mathrm{Pol}_K(r, d_O)$, and an integral element of this space has Fock valuation at least $n_0 - \kappa$, by a lemma that compares $v(\alpha!)$ with $v(\prod_i d_{O,i}!)$ for exponents $\alpha$ of degree $d_O$.

For clause 5, write $a = \langle F, \gamma\cdot\phi(Z)\rangle$ and $a' = \langle F, \gamma\cdot\phi(\Omega Z)\rangle$. We have $v(a) \leq n_0 + D_l + 1$ and $v(a' - a) \geq c + n_0 - 2\kappa - D_m$. The size hypothesis and $\kappa \geq 1$ give
$$c > 4(D_m + D_l + 3\kappa) \geq D_m + D_l + 2\kappa + 1,$$
so $v(a' - a) > v(a)$. By the ultrametric inequality $v(a') = v(a) \leq n_0 + D_l + 1$. The pairing is linear in its second argument, so $\langle F, \gamma\cdot\phi(G')\rangle = p^{N_2}a'$ and
$$\begin{aligned} v\big(p^{N_2}a'\big) - n_0 + \kappa &\leq D_l + 1 + N_2 + \kappa \\ &\leq D_m + D_l + \tfrac{3}{2}\kappa + 2 \\ &\leq E + 2\kappa. \end{aligned}$$
The last step uses $\kappa \geq 1$. $\square$

**Remark 5.1.14 (Formalization).** In the lift bound the polynomial $R$ is always $0$ (TestBoundOfRhoAndNormSets.lean:97). The parameter $C_0$ of Property PROJ and of the constant $e$ is not used (LiftBoundOfHypotheses.lean:168, 259), so $C_0$ plays no role. The parameter $p$ of the digit condition on $\gamma$ is not used (LiftBoundOfHypotheses.lean:326). The generic field `GLCoord` and the steps `stepB_of`, `stepC_of` and `stepDEF_of` were not unfolded; the proof states only their conclusions, which are the predicates `StepB`, `StepC` and `StepDEF` of CollapseExponent.lean:66 to 89. The comparison of factorials in clause 4 is `bge_of_cge` with `kapL_le_kap'`, also not unfolded.
