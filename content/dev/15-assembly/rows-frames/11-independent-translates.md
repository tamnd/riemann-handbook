---
title: Independent translates
decls:
  - GlobalTheory.TranslatesDet.independentTranslates
  - GlobalTheory.T.exists_cuspForm_nonzero_at_one_lift
  - GlobalTheory.LiftInterp.exists_form_one_lift
  - GlobalTheory.LiftInterp.comp_interp
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Independent translates

This section proves the theorem that [the cusp forms with independent translates](/entry/exists-cusp-form-independent-translates/) of section 10 states. That theorem is used by [the surjectivity from the hypotheses](/entry/onto-x-of-hypotheses-alt-alt/), in the surjectivity branch of [the unitary hypotheses](/proof/unitary-hypotheses/). The proof builds, for each component, one cusp form that is nonzero at one frame and zero at all other translates of that frame. A sum of these forms over the orbits gives a form whose matrix of translates is a permuted diagonal matrix.

### The setting

Let $E$ be a CM field with CM type $\Psi$, and let $r \geq 1$. A *datum* $X$ of rank $r$ over $E$ is a hermitian form of signature $(p_0, r - p_0)$ at each $\tau \in \Psi$, a lattice $\Lambda$ with a second lattice $L'$, an arithmetic group $\Gamma$ and a character $\chi$ of weights on $\Gamma$. A *frame* is a family $x = (x_\tau)_{\tau \in \Psi}$ of invertible $r \times r$ complex matrices. The *domain* is the set of frames whose leading Gram minors have the signs fixed by the signature. The group $\Gamma$ acts on frames on the left, and the Borel group $B$ of upper triangular matrices acts on the right. A *section of weight* $\lambda$ is a holomorphic function $P$ on the domain with

$$\begin{aligned} P(x b) &= b^{\lambda} P(x), \\ P(\gamma x) &= \chi(\gamma) P(x), \end{aligned}$$

for $b \in B$ and $\gamma \in \Gamma$. The space $SS(\lambda)$ is the space of bounded sections whose Fourier and Jacobi coefficients vanish at each isotropic vector. Its elements are the *cusp forms* of weight $\lambda$. A frame $x$ is *orthonormal* if its Gram matrix is the diagonal sign matrix of the signature. For an even integer $s$ the *determinant weight* $\nabla(s)$ has entry $-s/2$ at the first $p_0$ places of each $\tau$ and $s/2$ at the others.

A *two level datum* is a finite group $U$ acting on a finite set $C$, with a datum $X_c$ for each $c \in C$, and an element $\mathrm{tr}(u, c) \in GL_r(E)$ for each $u \in U$ and $c \in C$. The element $\mathrm{tr}(u, c)$ carries the lattices of $X_c$ to those of $X_{uc}$. All the data $X_c$ share $\Psi$, the hermitian form and $p_0$, and the character $\chi$ is trivial on each $\Gamma_c$. The element satisfies the cocycle rule

$$\mathrm{tr}(uv, c) \bigl(\mathrm{tr}(u, vc)\, \mathrm{tr}(v, c)\bigr)^{-1} \in \Gamma,$$

and it is *faithful*: if $uc = c$ and $\mathrm{tr}(u, c) \in \Gamma$, then $u = 1$. A form on the datum is a family $F = (F_c)$ with $F_c$ a section on the domain of $X_c$. The *pull* of $F$ by $h \in U$ is

$$(h^{*} F)(c, x) = F\bigl(hc, \mathrm{tr}(h, c)\, x\bigr).$$

The *determinant of translates* of $F$ at $(c, x)$ is the determinant of the $U \times U$ matrix whose entry at $(h, h')$ is $((h h')^{*} F)(c, x)$. The *upper level* at $c$ is the set of products $\gamma\, \mathrm{tr}(u, c)$ with $uc = c$ and $\gamma \in \Gamma_c$. It is a group that contains $\Gamma_c$. The datum is *unipotent over* a prime $g$ if for each such product $\beta$ we have $(\beta - 1)^r L' \subseteq g L'$. The *level hypothesis* asks for a prime $g$ with $3r < g$ that splits completely in $E$, such that the datum is unipotent over $g$.

Let $G \geq \Gamma$ be a group that stabilises $\Lambda$, let $x_0$ be a frame and let $\rho_0 > 0$. For frames $x$ put

$$\mathrm{rh}(x_0, x) = -\log \prod_{\tau \in \Psi} \frac{|d_{p_0}(x_\tau)|}{|m_{p_0}(x_{0,\tau}^{-1} x_\tau)|^{2}},$$

where $d_{p_0}$ is the leading Gram minor of size $p_0$ and $m_{p_0}$ is the leading minor of size $p_0$. The pair $(G, x_0)$ is a *free ball of radius* $\rho_0$ if for every $\gamma \in G$ with $\gamma \neq 1$, and every $x$ with $\mathrm{rh}(x_0, x) < \rho_0$, we have $\rho_0 \leq \mathrm{rh}(x_0, \gamma x)$. So the ball of radius $\rho_0$ around $x_0$ meets none of its translates.

### The interpolation on one component

**Lemma 7.11.1 (Interpolation on one component).** Let $X$ be a datum of rank $r$ over $E$ with $\chi = 1$ on $\Gamma$, and put $\dim X = |\Psi|\, p_0 (r - p_0)$. Let $g$ be a prime with $3r < g$ that splits completely in $E$. Let $G \geq \Gamma$ be a group of unitary stabilisers of both lattices, such that each $\beta \in G$ satisfies $(\beta - 1)^r L' \subseteq g L'$. Let $x$ be a frame of the domain at which $X$ has no contraction. Let $s$ be even with $s \geq 2r + 50 r^2 \dim X + 1$. Then there is $P \in SS(\nabla(s))$ with $P(x) \neq 0$ and $P(\gamma x) = 0$ for every $\gamma \in G$ with $\gamma \notin \Gamma$.

Lean: `GlobalTheory.LiftInterp.comp_interp`.

*Proof.* There are two cases.

1. Assume the form is definite, so $p_0 = 0$ or $p_0 = r$. Under the unipotence over $g$ and no contraction, a unitary stabiliser in $G$ of a definite lattice lies in $\Gamma$, so $G = \Gamma$. The condition on $\gamma$ is then empty. A determinant power section of weight $\nabla(s)$ that is nonzero at $x$ exists in the definite case, and it is a cusp form, since there are no isotropic vectors.
2. Assume $0 < p_0 < r$. The free ball lemma for the unitary upper level gives an orthonormal frame $x_0$ and $b \in B$ with $x = x_0 b$, such that $(G, x_0)$ is a free ball of radius $1/(49 r^2)$. [The orbit interpolation in the indefinite case](/entry/orbit-interpolation-det-weight-free-ball-indefinite/) then gives $P \in SS(\nabla(s))$ with $P(x_0) \neq 0$ and $P(\gamma x_0) = 0$ for $\gamma \in G \setminus \Gamma$.
3. In case 2 we have $P(x) = P(x_0 b) = b^{\nabla(s)} P(x_0)$, and $b^{\nabla(s)} \neq 0$ since $b$ is invertible. So $P(x) \neq 0$. For $\gamma \in G \setminus \Gamma$ we have $P(\gamma x) = b^{\nabla(s)} P(\gamma x_0) = 0$, since the left and right actions commute.

This proves the lemma. $\square$

### A form that sees one lift

**Theorem 7.11.2 (A cusp form nonzero at one lift).** Let a two level datum of rank $r$ over $E$ satisfy the level hypothesis. Let $c \in C$, let $x$ be a frame of the domain of $X_c$ at which the datum has no contraction, and let $s$ be even with $s \geq 2r + 50 r^2 \dim X + 1$. Then there is a form $u$ of weight $\nabla(s)$, with $u_{c'}$ a cusp form for each $c'$, such that the following hold.

1. $u(c, x) \neq 0$.
2. $(h^{*} u)(c, x) = 0$ for every $h \in U$ with $h \neq 1$.
3. $u_{c'} = 0$ for every $c'$ outside the orbit $U c$.

Lean: `GlobalTheory.T.exists_cuspForm_nonzero_at_one_lift` (also `GlobalTheory.LiftInterp.exists_form_one_lift`).

*Proof.* We take the steps in order.

1. The level hypothesis gives a prime $g$ with $3r < g$ that splits completely, such that the datum is unipotent over $g$.
2. The upper level $G_c$ at $c$ is a subgroup of $GL_r(E)$ that contains $\Gamma_c$. Its elements are unitary stabilisers of both lattices of $X_c$, since each $\mathrm{tr}(u, c)$ with $uc = c$ preserves the hermitian form and the lattices. They are unipotent over $g$ by the level hypothesis.
3. [The interpolation on one component](/entry/comp-interp/) gives $P \in SS(\nabla(s))$ for $X_c$ with $P(x) \neq 0$ and $P(\gamma x) = 0$ for $\gamma \in G_c \setminus \Gamma_c$.
4. Put $u_c = P$ and $u_{c'} = 0$ for $c' \neq c$. Each $u_{c'}$ is a cusp form, and clauses 1 and 3 hold.
5. Let $h \neq 1$. If $hc \neq c$, then $(h^{*} u)(c, x) = u_{hc}(\ldots) = 0$. If $hc = c$, then $\beta = \mathrm{tr}(h, c)$ lies in $G_c$. It does not lie in $\Gamma_c$, since the datum is faithful and $h \neq 1$. So $(h^{*} u)(c, x) = P(\beta x) = 0$.

This proves the theorem. $\square$

The form $u$ is in fact zero off the single component $c$, which is stronger than clause 3.

### The sum over the orbits

**Theorem 7.11.3 (Independent translates).** Let $E$ be CM, let a two level datum of rank $r$ over $E$ satisfy the level hypothesis, and let $s$ be even with
$$s \geq 2r + 50 r^2 \dim X + 1.$$
Then there is a form $u_0$ of weight $\nabla(s)$ with each component a cusp form, such that for each $c \in C$ some frame $x$ of the domain of $X_c$ has a nonzero determinant of translates of $u_0$ at $(c, x)$.

Lean: `GlobalTheory.TranslatesDet.independentTranslates`.

*Proof.* We take the steps in order.

1. For each $c$ the balanced frame theorem for CM unitary data gives a frame $x_c$ of the domain of $X_c$ at which the datum has no contraction: every endomorphism of $L'$ of norm less than $1$ at $x_c$ is zero.
2. Choose a set $R \subseteq C$ of representatives of the orbits of $U$. For $q \in R$ let $u_q$ be the form of [the cusp form nonzero at one lift](/entry/exists-cusp-form-nonzero-at-one-lift/) at $(q, x_q)$. Put $u_0 = \sum_{q \in R} u_q$. A finite sum of cusp forms is a cusp form, so each component of $u_0$ is a cusp form.
3. Let $c \in C$. Then $c = k c_0$ for some $c_0 \in R$ and $k \in U$. Put $x_0 = x_{c_0}$ and $x = \mathrm{tr}(k, c_0)\, x_0$. The frame $x$ lies in the domain of $X_c$, since $\mathrm{tr}(k, c_0)$ carries the hermitian structure of $X_{c_0}$ to that of $X_c$.
4. For $q \in R$ with $q \neq c_0$, the form $u_q$ vanishes on the orbit of $c_0$, so it gives no term. So the entries of the matrix of translates at $(c, x)$ are those of $u_{c_0}$.
5. By the cocycle rule, $((h h')^{*} u_{c_0})(c, x)$ is equal to $u_{c_0}$ at $(h h' k c_0, \beta x_0)$ for some $\beta$ with $\beta \equiv \mathrm{tr}(h h' k, c_0)$ modulo $\Gamma$, and $\chi = 1$ removes the factor in $\Gamma$. By clause 2 of the previous theorem it is zero unless $h h' k = 1$, and it is $u_{c_0}(c_0, x_0)$ if $h h' k = 1$.
6. So the matrix is $a$ times the permutation matrix of $h \mapsto h' = h^{-1} k^{-1}$, with $a = u_{c_0}(c_0, x_0) \neq 0$. Its determinant is $\pm a^{|U|} \neq 0$.

This proves the theorem. $\square$

This is the statement of section 10, where $\dim X = |\Psi|\, p_0 (r - p_0)$. The proof uses only the no contraction property of the balanced frames. The second output of the balanced frame theorem, that there is no short vector, is not used.

**Remark 7.11.4 (Formalization).** The two level datum, the pull, the determinant of translates and the goal `IndependentTranslates` are in [TwoLevelLogarithm.lean](lean:Development/AbelianVarietyTheory/BlockTheory/PoincareCuspForms/TwoLevelLogarithm.lean#L28), with the goal at line 99. The main proof is at line 187 of [ExistsCuspFormIndependentTranslates.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCuspFormIndependentTranslates.lean#L187). The helpers at lines 20 to 121 move frames between components (`domOfComp`, `domToComp`, `trDom`) and close the cusp forms under the left action, zero, sums and finite sums (`ssLact`, `ssZero`, `ssAdd`, `ssSum`). The permuted diagonal determinant is the lemma `detNeAt` at line 134. The `NoShortVector` output of `existsBalancedFrameCMUnitary_proof` is dropped by a pattern at lines 187 to 192. The statement `T.exists_cuspForm_nonzero_at_one_lift` at line 7 of [ExistsCuspFormNonzeroAtOneLiftStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCuspFormNonzeroAtOneLiftStatement.lean#L7) is a `first | exact` wrapper under `maxHeartbeats 1000000`. The proof `exists_form_one_lift` at line 75 of [ExistsCuspFormNonzeroAtOneLift.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsCuspFormNonzeroAtOneLift.lean#L75) builds $u$ supported on the single component $c$, and `comp_interp` at line 32 splits into the definite and indefinite cases. The free ball predicate is `Up.FreeBall` at line 23 of [FreeBallIffOfDimXEqZero.lean](lean:Development/AbelianVarietyTheory/Definitions/UpperBounds/FreeBallIffOfDimXEqZero.lean#L23).
