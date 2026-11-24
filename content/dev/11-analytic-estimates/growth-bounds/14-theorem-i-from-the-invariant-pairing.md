---
title: Theorem I from the invariant pairing
decls:
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_closed_form_holds
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_pairing_GL
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_contraction
  - Formalism.MainNotions.flipOneThree.Pf.contraction_of_pairing_GL
  - Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_two_letter_clauses_contraction
  - Formalism.MainNotions.flipOneThree.Pf.cloud_maps_of_contraction
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Theorem I from the invariant pairing

This section proves the closed form of Theorem I at every datum. Section 13 reduced it, in [the Theorem (Theorem I from the explicit minor map)](/entry/theorem-i-of-explicit-minor-map/), to the explicit minor map statement and the cloud maps statement. Both come from one construction on dual Weyl modules: an invariant pairing between a module of a weight $\alpha$ and the module of the complementary weight, with dual bases whose pairings are powers of $p$ with small exponents. From the pairing we build a contraction to the standard weight $\omega_{P,Q}$, and from the contraction the cloud maps. The closed form is one of the two main inputs of [the first theorem with constants](/entry/first-theorem-with-constants/) of Section 16.

We keep the notation of Sections 12 and 13. For $r \geq 1$ and a nonincreasing $\nu \in \mathbb{Z}^r$, let $S_\nu \subseteq K[X_{ij}]$ be the dual Weyl module of weight $\nu$ in an $r \times r$ matrix of variables, and $S_\nu(\mathcal{O})$ the image of the dual Weyl module over $\mathcal{O}$; a matrix $l$ acts on polynomials by the substitution $X \mapsto lX$ of rows. For a weight $\mu$ put $\mu^*_i = -\mu_{r-1-i}$, the dual weight. Polynomials in two matrices are written $f \otimes f'$ for $f$ in the first and $f'$ in the second. Let $\lambda_a = \log_p(8a + m) + 1$ as before, and write $\kappa_1(r) = \lceil r^2(\log_p(8a + r) + 1)\rceil$.

### The pairing and the contraction

**Definition 5.14.1 (Invariant pairing).** The *invariant pairing statement* holds if for every setting, every $r \geq 1$, all $a, c, N$ and every nonincreasing $\alpha \in \mathbb{N}^r$ with $\alpha_i \leq N$, $\alpha_i \leq \alpha_j + c$ for all $i, j$ and $c \leq 8a$, with $\alpha'_i = N - \alpha_{r-1-i}$, there is a linear form $L$ on polynomials in two $r \times r$ matrices such that:

1. $L(lf \otimes lf') = \det(l)^N L(f \otimes f')$ for every invertible $l$, $f \in S_\alpha$ and $f' \in S_{\alpha'}$;
2. $L(f \otimes f') \in \mathcal{O}$ for $f \in S_\alpha(\mathcal{O})$ and $f' \in S_{\alpha'}(\mathcal{O})$;
3. there are $u_b \in S_\alpha(\mathcal{O})$ and $u'_b \in S_{\alpha'}(\mathcal{O})$, for $b$ in a set of size the Weyl dimension of $\alpha$, and exponents $k_b \leq \kappa_1(r + 1)$, with $L(u_b \otimes u'_{b'}) = p^{k_b}$ if $b = b'$ and $0$ otherwise.

Over a field of characteristic $0$ the dual of $S_\alpha$ is $S_{\alpha'}$ twisted by $\det^{-N}$, so a pairing with the first property exists and is perfect. The content is the integrality and the bound on the exponents.

**Proposition 5.14.2 (Invariant pairing).** The invariant pairing statement holds.

Lean: `Formalism.MainNotions.flipOneThree.Pf.qPh_proved`.

*Proof.* Let $e = \min_i\alpha_i$. Every $f \in S_\alpha$ is $\det^e f_0$ with $f_0 \in S_{\alpha - e}$, and $\det$ is multiplied by $\det l$ under the row action. A map $\tau$ carries $S_{\alpha'}$ to $S_{\alpha - e}$, integrally and onto the integral module, compatibly with the row action. A Smith form gives a bilinear form $B$ on $S_{\alpha - e}$ with $B(lP, Q) = B(P, l^TQ)$, integral on the integral module, with dual bases of size the Weyl dimension and exponents at most an explicit bound. Pair $f_0$ with $\tau(f')$ by $B$. A numerical lemma shows that the exponent bound is at most $\kappa_1(r + 1)$, using $\alpha_i - e \leq c \leq 8a$. $\square$

**Definition 5.14.3 (Contraction to the standard lattice).** Let $m \geq 2$ and $n = m + 1$. The *contraction statement* holds if for every setting, all $a, c, P, Q$ and every nonincreasing $\lambda \in \mathbb{Z}^n$ with $\lambda_0 = P + c$, $\lambda_{n-1} = -(Q + c)$, $|\lambda_i| \leq c$ for $0 < i < m$ and $2c \leq 8a$, there is a linear map $\Phi$ from polynomials in two $n \times n$ matrices to polynomials in one, with $\mu = \lambda - \omega_{P,Q}$, such that:

1. $\Phi(v \otimes t) \in S_{\omega_{P+2c,Q+2c}}$ for $v \in S_\lambda$ and $t \in S_{\mu^*}$;
2. $\Phi(lv \otimes lt) = l\,\Phi(v \otimes t)$ for every invertible $l$;
3. $\Phi$ carries $S_\lambda(\mathcal{O}) \otimes S_{\mu^*}(\mathcal{O})$ into $S_{\omega_{P+2c,Q+2c}}(\mathcal{O})$;
4. there are $s_b \in S_\mu(\mathcal{O})$ and $s'_b \in S_{\mu^*}(\mathcal{O})$, with all monomials of degree $2c$ in the first row, for $b$ in a set of size the Weyl dimension of the middle part $(\lambda_1, \dots, \lambda_{m-1})$, and exponents $k_b \leq \kappa_1(m)$, such that for every $F \in S_{\omega_{P,Q}}$
$$\Phi(Fs_b \otimes s'_{b'}) = \begin{cases} p^{k_b}\,h_{2c}F, & b = b', \\ 0, & b \neq b', \end{cases}$$
where $h_{2c}$ is the highest weight vector of $S_{\omega_{2c,2c}}$.

So $\Phi$ splits $S_\lambda$ into copies of $S_{\omega_{P,Q}}$ indexed by a basis of the middle part, up to the powers $p^{k_b}$.

**Theorem 5.14.4 (Contraction from the invariant pairing).** The invariant pairing statement and the Cartan surjectivity (the sections of weight $\lambda + \mu$ are spanned over $\mathcal{O}$ by products of sections of weights $\lambda$ and $\mu$) imply the contraction statement.

Lean: `Formalism.MainNotions.flipOneThree.Pf.contraction_of_pairing_GL`.

*Proof.* Apply the invariant pairing to the middle block of size $r = m - 1$, and extend it to $n \times n$ matrices by the substitution of coefficients, which commutes with the row action and keeps the integral modules. Division by powers of $\det$ and the integral cap (a polynomial of $S_\nu$ with integral coefficients lies in $S_\nu(\mathcal{O})$) give the integrality; the highest weight vectors multiply as $h_{2c}F$. Two lemmas, on the middle weights and on the top line, use the explicit minor map, the Gauss inverse lemma for two-letter lattices and the Cartan surjectivity. All other inputs are proved. $\square$

### The cloud maps

For a base weight $(a_w, b_w, \lambda_0)$ on $T$ with constant $c$, let the *cloud* of $\lambda_{0,s}$ be its middle part, and let $d_{\mathrm{cl}}(\lambda_0) = \prod_{s \in T}\dim$ of the representation of the cloud of $\lambda_{0,s}$, a product of Weyl dimensions.

**Definition 5.14.5 (Cloud maps).** The *cloud maps statement* holds if for every setting, every $m \geq 2$, $T$, $a$, $c$, every base weight $(a_w, b_w, \lambda_0)$ with $\lambda_0$ dominant and $0$ off $T$, $A = a_w - c$, $B = b_w - c$, $2c \leq 8a$, and every edge $e$ of rank $1$, with $\lambda_1 = \mathrm{fl}(A, B)$ and $\lambda_2 = \mathrm{fl}(A + 2c, B + 2c)$, there are maps $\iota : V_{\lambda_1} \to V_{\lambda_2}$, $U_b : V_{\lambda_1} \to V_{\lambda_0}$ and $L_b : V_{\lambda_0} \to V_{\lambda_2}$, for $b$ in a set of size $d_{\mathrm{cl}}(\lambda_0)$, and exponents $k_b \leq |T|\kappa_1(m)$, such that:

1. $L_{b'}U_b = p^{k_b}\iota$ if $b = b'$ and $0$ otherwise;
2. $\iota(F) \in R_e$ if and only if $F \in R_e$;
3. for $c_2 \geq 2|T|c$ and all $t$: $\iota$ and each $U_b$ carry the cleaned module $C(t, c_2, e)$ of $\lambda_1$ into those of $\lambda_2$ and $\lambda_0$, and for $g$ in the dual cleaned module $C'(t, c_2, e)$ of $\lambda_2$, $p^{A(\lambda_2) - A(\lambda_0)}\,g \circ L_b$ lies in the dual cleaned module $C'(t, c_2 - 2|T|c, e)$ of $\lambda_0$, where $A(\lambda)$ is the shift of the lattice $R'_e$ at rank $1$.

The maps $U_b$ and $L_b$ realize $V_{\lambda_0}$ between two flat weights, up to the small factors $p^{k_b}$. This is what the cloud weight bound of Section 12 needs.

**Theorem 5.14.6 (Cloud maps from the contraction).** The contraction statement, the two Cartan statements (a product $FG$ of sections divisible by $w$ has a factor divisible by $w$, and the Cartan surjectivity) and the dual height inclusion ($H(\mathrm{src}\,e) \subseteq R_e$ and $H(\mathrm{tgt}\,e)^\vee \subseteq R'_e$ for every edge) imply the cloud maps statement.

Lean: `Formalism.MainNotions.flipOneThree.Pf.cloud_maps_of_contraction`.

*Proof.* For one $s \in T$ apply the contraction with $(P, Q) = (A_s, B_s)$ and $\lambda = \lambda_{0,s}$, so that $\mu + \omega_{P,Q} = \lambda$. The maps $U_b(F) = Fs_b$ from $S_{\omega_{P,Q}}$ to $S_\lambda$ and $L_b(v) = \Phi(v \otimes s'_b)$ from $S_\lambda$ to $S_{\omega_{P+2c,Q+2c}}$ satisfy $L_{b'}U_b(F) = \delta_{bb'}p^{k_b}h_{2c}F$ by the fourth property, so $\iota$ is multiplication by $h_{2c}$ in this factor. The two Cartan statements identify the lattice of sections of a sum of weights with the $\mathcal{O}$-span of products of sections, and so carry the integrality of $\Phi$ and of $s_b, s'_b$ over to the lattices $H^0(\cdot, \Lambda)$ for every lattice $\Lambda$. Taking the tensor product over $s \in T$ adds the exponents, which gives $k_b \leq |T|\kappa_1(m)$, and multiplies the counts, which gives $d_{\mathrm{cl}}(\lambda_0)$. The dual height inclusion places the images in the cleaned modules. $\square$

### The closed form

**Theorem 5.14.7 (Theorem I from the two-letter clauses and the contraction).** Assume that $\Psi$ is injective for $m \geq 1$, that $\Psi(\mathrm{Pol}_{P,Q}) = \mathrm{Two}(P, Q)$, the *Gauss inverse lemma* (for an invertible matrix $g$ and $g' = g^{-1}$, $\Psi(f)$ lies in the two-letter lattice of the column span of $g$ if and only if $f$ lies in $g'$ times the Gauss lattice), and the contraction statement. Then the closed form of Theorem I holds for every datum.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_two_letter_clauses_contraction`.

*Proof.* Let $\mathcal{D}$ be admissible for large constants and take the tools at $C_c = 4$. They contain the two Cartan statements, the dual height inclusion and the third condition on column systems. The three clauses, the Cartan surjectivity and that condition give the explicit minor map statement: the remaining parts, $\delta\Psi(\mathrm{Pol}_{a,b}) = S_{a,b}$ with kernel $h\,\mathrm{Pol}_{a-1,b-1}$ and the lattice $H^0(\omega_{a,b}, \Lambda)$, come from the surjectivity onto products. The Theorem (Cloud maps from the contraction) gives the cloud maps. Apply [the Theorem (Theorem I from the explicit minor map)](/entry/theorem-i-of-explicit-minor-map/). $\square$

**Theorem 5.14.8 (Theorem I from the contraction).** The contraction statement implies the closed form of Theorem I for every datum.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_contraction`.

*Proof.* The three clauses on $\Psi$ are proved: the injectivity, the image of $\mathrm{Pol}_{P,Q}$ and the Gauss inverse lemma. Apply the Theorem (Theorem I from the two-letter clauses and the contraction). $\square$

**Theorem 5.14.9 (Theorem I from the invariant pairing).** The invariant pairing statement implies the closed form of Theorem I for every datum.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_pairing_GL`.

*Proof.* Let $\mathcal{D}$ be admissible for large constants. At $C_c = 0$ the thresholds give the twelve tools, and among them the Cartan surjectivity. With it the Theorem (Contraction from the invariant pairing) gives the contraction statement, and the Theorem (Theorem I from the contraction) gives the closed form. $\square$

**Theorem 5.14.10 (Closed form of Theorem I).** For every datum $\mathcal{D}$: if $\mathcal{D}$ is admissible for Theorem I for large constants, then there is $T_0 > 0$ such that for every $C_0 \geq T_0$ there are $T_2, C > 0$ with Theorem I with constants $(C_0, C_H, C)$ for all $C_H \geq T_2$.

Lean: `Formalism.MainNotions.flipOneThree.Pf.theorem_I_closed_form_holds` (also `Formalism.MainNotions.flipOneThree.Pf.restCloudMaps_proved`, the cloud maps statement under the Cartan statements and the dual height inclusion).

*Proof.* This is the Theorem (Theorem I from the invariant pairing) applied to the Proposition (Invariant pairing). $\square$

So the only inputs of Theorem I are the five conditions of admissibility for Theorem I, among them the twelve tools.

**Remark 5.14.11 (Formalization).** `theorem_I_of_pairing_GL` (HermitianTensor/ModelIdentificationHolds.lean:25) takes the Cartan surjectivity from the admissibility at $C_c = 0$, while `theorem_I_of_two_letter_clauses_contraction` (HermitianTensor/TheoremIOfTwoLetterClausesContraction.lean:15) takes the tools at $C_c = 4$; both work because the tools do not depend on the constants. The Cartan surjectivity is also proved outright as `cartanOnto_proved` (LocalToGlobal/GroupLattices/FockModels/Cartan.lean:263), which these proofs do not use. The assembly lemmas `qPh_of` and `contraction_of_pairing_lemmas`, the map `tiePsi_of`, the pieces `cloudOne_of`, `restCloudLat_of`, `cloudIso` and `restCloudMaps_of`, and the proofs of the three clauses on $\Psi$ were not unfolded; the proofs above follow the statements of their inputs. The map called `abelian₂` in the contraction statement is $\Phi$. The definitions `GradedLatticeStable` and `TypeDecompositionsCommute` ignore their datum (ProjectionLemmaBaseLevel.lean:217 and 221).
