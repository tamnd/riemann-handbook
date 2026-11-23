---
title: Harmonic polynomials and the frame reading
decls:
  - GlobalTheory.WeightOrderLemmas.main_field
  - GlobalTheory.WeightOrderLemmas.main
  - GlobalTheory.FrameRead.cof_image
  - GlobalTheory.T.hodge_weight_dominance_condition
  - GlobalTheory.FrameRead.CoefMap.exists_ioLFRec
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Harmonic polynomials and the frame reading

The theta rules of this volume are built from harmonic polynomials in the letters of a datum. This section identifies the space of such polynomials of a fixed row degree with a tensor product of dual Weyl modules of $\mathrm{GL}_n$. The identification is a substitution of variables, the frame reading, followed by division by a power of determinants. It is injective, it is onto, and it intertwines the two actions of $\mathrm{GL}_n$. From it we build the record that the [record of harmonic inputs](/entry/exists-io-record/) needs: a linear isomorphism from the tensor product onto the span of the harmonic polynomials, with a highest weight vector that goes to a product of leading minors. The classical background is the [Fock model](/learn/theta/#the-fock-model) and [highest weights](/learn/representations/#highest-weights-and-branching).

### Letters and harmonic polynomials

Let $E$ be a CM [[number field|MWBDFS2KJ5]] with complex conjugation $\tau \mapsto \bar\tau$ on its embeddings $\tau : E \to \mathbb{C}$. A datum over a host of $E$ fixes integers $p, q$, a multiplicity $m_\tau \geq 0$ for each embedding, and a set $\Psi$ of embeddings that contains exactly one of $\tau, \bar\tau$ for each pair. Fix $n \geq 0$ and a field $K$.

**Definition 2.1.1 (letters).** A *letter* is a triple $(\tau, i, b)$ with $\tau : E \to \mathbb{C}$, $0 \leq i < m_\tau$ and $0 \leq b < n$. The pair $(\tau, i)$ is its *row* and $b$ is its *column*. We write $X_{\tau, i, b}$ for the variables of the polynomial ring $K[X]$ in the letters.

**Definition 2.1.2 (harmonic polynomials of row degree $a$).** Let $a(\tau, i) \in \mathbb{N}$. A polynomial $P \in K[X]$ lies in $\mathcal{H}_a$ if the following three conditions hold.

1. *Harmonic.* For every $\tau \in \Psi$, every $i < m_\tau$ and every $i' < m_{\bar\tau}$,
$$\sum_{b=0}^{n-1} \frac{\partial^2 P}{\partial X_{\tau, i, b}\, \partial X_{\bar\tau, i', b}} = 0.$$
2. *Row invariant.* For every $\tau$, all $i' < i < m_\tau$ and every $t \in K$, $P$ is fixed by the substitution $X_{\tau, i, b} \mapsto X_{\tau, i, b} + t X_{\tau, i', b}$ for all $b$, with the other letters fixed.
3. *Row degree.* Every monomial of $P$ has total degree $a(\tau, i)$ in the letters of row $(\tau, i)$.

When $K$ is the coefficient field $F$ of a level, we write $\mathcal{H}_a^{\mathcal{O}}$ for the set of $P \in \mathcal{H}_a$ whose coefficients lie in the ring of integers $\mathcal{O}_F$.

The first condition says that $P$ is killed by the Laplace operators that pair a row of $\tau$ with a row of $\bar\tau$. These are the harmonic polynomials of Kashiwara and Vergne in the Fock model of the [[Weil representation|CD20HVR9V8]].

### Dual Weyl modules

**Definition 2.1.3 (dominant weights).** A *dominant weight* of size $n$ is a nonincreasing function $\lambda : \{0, \dots, n-1\} \to \mathbb{Z}$. Its *shift* is $\lambda(n-1)$ when $n > 0$ and $0$ when $n = 0$. Its *reduced weight* is $\lambda^\circ(i) = \lambda(i) - \lambda(n-1) \geq 0$.

**Definition 2.1.4 (dual Weyl module).** Let $\nu : \{0, \dots, n-1\} \to \mathbb{N}$. In the polynomial ring $K[Y_{a,s}]$ in the entries of an $n \times n$ matrix $Y$, the module $\nabla(\nu)$ is the set of polynomials $f$ such that every monomial of $f$ has degree $\nu(s)$ in column $s$, and $f$ is fixed by the column operation $C_j \mapsto C_j + t C_l$ for all $l < j$ and all $t$.

Let $I$ be a finite index set. For $\lambda : I \to$ dominant weights, take one matrix of variables $Y^{(t)}$ for each $t \in I$. Let $V(\lambda)$ be the $K$-span of all products $\prod_{t} f_t(Y^{(t)})$ with $f_t \in \nabla(\lambda_t^\circ)$. This is the tensor product of the dual Weyl modules of the reduced weights. The group $\prod_t \mathrm{GL}_n(K)$ acts on $V(\lambda)$ by
$$(g \cdot F)\bigl(Y^{(t)}\bigr) = \prod_t \det(g_t)^{\lambda_t(n-1)} \cdot F\bigl(g_t^{\mathsf{T}} Y^{(t)}\bigr).$$

### The frame reading

Fix an injective map $t \mapsto \tau_t$ from $I$ to the embeddings of $E$, with image exactly $\Psi$. Fix $a$, integers $s_t$ and dominant weights $\lambda_t$ of size $n$.

**Definition 2.1.5 (frame reading).** The frame reading is the $K$-algebra map $\mathrm{cof} : K[X] \to K[Y^{(t)} : t \in I]$ with
$$\mathrm{cof}(X_{\tau, i, b}) = \begin{cases} Y^{(t)}_{b, i} & \text{if } \tau = \tau_t \text{ and } i < n, \\ \operatorname{adj}(Y^{(t)})_{n-1-i,\, b} & \text{if } \tau = \bar\tau_t \text{ and } i < n, \\ 0 & \text{otherwise.} \end{cases}$$
Here $\operatorname{adj}$ is the adjugate matrix.

**Definition 2.1.6 (weight condition and determinant factor).** The weights *match* if for every $t$ and every $i < n$
$$\lambda_t(i) = s_t + [\,i < m_{\tau_t}\,]\, a(\tau_t, i) - [\,n-1-i < m_{\bar\tau_t}\,]\, a(\bar\tau_t, n-1-i),$$
where $[\cdot]$ is $1$ if the condition holds and $0$ if not. Put $\deg_c(t) = \sum_{i < m_{\bar\tau_t}} a(\bar\tau_t, i)$ and
$$D = \prod_{t \in I} \det\bigl(Y^{(t)}\bigr)^{\max(0,\ \deg_c(t) + \lambda_t(n-1) - s_t)}.$$

**Definition 2.1.7 (letter action).** For $g = (g_t) \in \prod_t \mathrm{GL}_n(K)$, the letter action is the $K$-algebra map with $X_{\tau_t, i, b} \mapsto \sum_j g_t(j, b) X_{\tau_t, i, j}$ and $X_{\bar\tau_t, i, b} \mapsto \sum_j g_t^{-1}(b, j) X_{\bar\tau_t, i, j}$, fixing the letters of embeddings outside $\Psi \cup \bar\Psi$.

**Theorem 2.1.8 (frame reading of harmonic polynomials).** Let $K$ be a field with a ring map $\varphi : K \to \mathbb{C}$. Assume $p + q \leq n$, that $i \mapsto a(\tau, i)$ is nonincreasing for every $\tau$, and that the weights match. Then:

1. for every $P \in \mathcal{H}_a$ there is $F \in V(\lambda)$ with $\mathrm{cof}(P) = D \cdot F$;
2. for every $F \in V(\lambda)$ there is exactly one $P \in \mathcal{H}_a$ with $\mathrm{cof}(P) = D \cdot F$;
3. if $P \in \mathcal{H}_a$, $F \in V(\lambda)$ and $\mathrm{cof}(P) = D \cdot F$, then for every $g$,
$$\mathrm{cof}(g \ast P) = \prod_t \det(g_t)^{-s_t} \cdot D \cdot (g \cdot F),$$
where $g \ast P$ is the letter action.

Lean: `GlobalTheory.WeightOrderLemmas.main_field`.

*Proof.* The rows of letters split into the rows of $\tau_t$, which we call $x$-rows, and the rows of $\bar\tau_t$, which we call $y$-rows. A renaming of variables moves the three conditions of $\mathcal{H}_a$ to this indexing. Under it, harmonicity becomes the vanishing of the Laplace operators $\sum_b \partial_{x_{t,i,b}} \partial_{y_{t,i',b}}$, and the frame reading becomes the substitution of $x$-rows by rows of $Y^{(t)}$ and of $y$-rows by rows of $\operatorname{adj}(Y^{(t)})$, read from the bottom. We use five steps. The field $K$ has characteristic $0$, since it embeds in $\mathbb{C}$.

*Step 1: the image lies in a tensor product.* Let $\mu_t$ be the weight of $Y^{(t)}$ that the substitution gives to a monomial of row degree $a$. A row invariant polynomial of row degree $a$ maps into the span of products of elements of $\nabla(\mu_t)$. Row invariance in $x$ and $y$ becomes column invariance in $Y^{(t)}$, because the rows of the adjugate are the cofactor rows.

*Step 2: division by determinants.* The weight condition gives $\mu_t = \lambda_t^\circ + e_t$ with $e_t = \max(0, \deg_c(t) + \lambda_t(n-1) - s_t)$. Since $\lambda_t^\circ$ is nonincreasing, an element of the tensor product of the $\nabla(\mu_t)$ is $\prod_t \det(Y^{(t)})^{e_t}$ times an element of $V(\lambda)$, and conversely. This gives claim 1.

*Step 3: injectivity.* Let $P$ be harmonic of row degree $a$ with $\mathrm{cof}(P) = 0$. The kernel of the substitution is the ideal generated by the quadratic invariants $\sum_b x_{t,i,b} y_{t,i',b}$. Apply $\varphi$ to the coefficients. In the Fock inner product on complex polynomials, the adjoint of multiplication by $\sum_b x_b y_b$ is the Laplace operator $\sum_b \partial_{x_b}\partial_{y_b}$. So a harmonic polynomial is orthogonal to the ideal. Since $P$ is in the ideal and harmonic, it is orthogonal to itself, and $P = 0$.

*Step 4: surjectivity.* Each dual Weyl module $\nabla(\nu)$ with $\nu$ nonincreasing is irreducible in the following sense: a nonzero subspace over $\mathbb{Q}$ of $\nabla(\nu)$ that is stable under $\mathrm{GL}_n(\mathbb{Q})$ spans $\nabla(\nu)$ over $K$. The images of row invariant polynomials of row degree $a$ form such a subspace in each factor, so every element of the tensor product of the $\nabla(\mu_t)$ is the image of a row invariant polynomial of row degree $a$. Here the monotony of $a$ is used, since it makes $\mu_t$ nonincreasing. Then replace this polynomial by its harmonic part. By the orthogonal decomposition of Step 3, every polynomial is a harmonic polynomial plus an element of the ideal. The harmonic part keeps the row degree and the row invariance, and it has the same image. Uniqueness in claim 2 comes from Step 3.

*Step 5: equivariance.* The letter action by $g$ becomes $Y^{(t)} \mapsto g_t^{\mathsf{T}} Y^{(t)}$ on the $x$-rows. On the $y$-rows the inverse matrix acts on the adjugate, which gives $\operatorname{adj}(g_t^{\mathsf{T}} Y^{(t)})$ times the scalar $\det(g_t)^{-1}$ for each letter of a $y$-row. A monomial of row degree $a$ has $\deg_c(t)$ such letters for each $t$. The factor $D$ transforms by $\prod_t \det(g_t)^{e_t}$, and $V(\lambda)$ carries the extra factor $\det(g_t)^{\lambda_t(n-1)}$. The exponents add up to $-s_t$, by the definition of $e_t$. This gives claim 3. $\square$

**Corollary 2.1.9 (the frame reading over the coefficient field).** Let $F \subset \mathbb{C}$ be the coefficient field of a level. Under the hypotheses of the Theorem, with $K = F$, the three claims hold.

Lean: `GlobalTheory.WeightOrderLemmas.main` (also `GlobalTheory.FrameRead.cof_image` and `GlobalTheory.T.hodge_weight_dominance_condition`, second names).

*Proof.* This is the Theorem applied to $K = F$ and the inclusion $F \subset \mathbb{C}$. $\square$

### The harmonic record

The Corollary lets us transport the integral structure of $V(\lambda)$ to harmonic polynomials. Let $F$ be the coefficient field of a level and $\mathcal{O}_F$ its ring of integers. The space $V(\lambda)$ carries an $\mathcal{O}_F$-lattice $V_0$ attached to the standard lattice $\mathcal{O}_E^n$, and an action $\rho$ of $\mathrm{GL}_n(E)$ through the embeddings $\tau_t$. Let $w \in V(\lambda)$ be the tensor product of the extremal vectors: for each $t$, the product of the leading principal minors of $Y^{(t)}$ with exponents $\lambda^\circ_t(k) - \lambda^\circ_t(k+1)$. Let $G \in F[X]$ be the product over all rows $(\tau, i)$ of the leading minor of size $i + 1$ of the letters of $\tau$, raised to $a(\tau, i) - a(\tau, i+1)$, where $a(\tau, m_\tau) = 0$. The minor uses the first $i + 1$ columns if $\tau \in \Psi$ and the last $i + 1$ columns if not. For a matrix $\gamma$ over $E$, let $\gamma^\star$ be the substitution of letters $X_{\tau, i, b} \mapsto \sum_j \tau(\gamma_{j b}) X_{\tau, i, j}$ in the form of the letter forms of $\gamma$.

**Theorem 2.1.10 (the harmonic record).** Under the hypotheses of the Corollary there are an $F$-linear map $\iota : V(\lambda) \to F[X]$ and a vector $w \in V(\lambda)$ such that $w$ is the tensor product of the extremal vectors and there is a function $c$ on $n \times n$ matrices over $E$ with:

1. $p + q \leq n$, and $\iota$ is injective;
2. the image of $\iota$ is the $F$-span of $\mathcal{H}_a$;
3. for every $\gamma$ with $\gamma^\ast \gamma = 1$ and every $v$, $\iota(\rho(\gamma) v) = c(\gamma) \cdot \bar\gamma^\star(\iota v)$, where $\bar\gamma$ is the entrywise conjugate;
4. $w \in V_0$, and if $s \in F$ has $s w \in V_0$ then $s \in \mathcal{O}_F$;
5. $\iota(w) = G$;
6. $\mathcal{H}_a^{\mathcal{O}} \subseteq \iota(V_0)$.

Lean: `GlobalTheory.FrameRead.CoefMap.exists_ioLFRec`.

*Proof.* A lemma on leading minors gives a sign $\varepsilon = \pm 1$ with $\mathrm{cof}(G) = \varepsilon \cdot D \cdot w$. For $v \in V(\lambda)$, let $\iota(v)$ be the unique $P \in \mathcal{H}_a$ with $\mathrm{cof}(P) = \varepsilon D v$, which exists by claim 2 of the Corollary. Uniqueness makes $\iota$ linear.

Injectivity: if $\iota(v) = 0$, then $\varepsilon D v = 0$. Since $D \neq 0$ and the polynomial ring is a domain, $v = 0$. The image is all of $\mathcal{H}_a$: given $P \in \mathcal{H}_a$, claim 1 gives $F$ with $\mathrm{cof}(P) = D F$, and then $\iota(\varepsilon F) = P$ because $\varepsilon^2 = 1$. Since $\mathcal{H}_a$ is a subspace, its span is itself. This gives claims 1 and 2.

The product of minors $G$ lies in $\mathcal{H}_a$, by a separate lemma on minor products. Claim 1 of the Corollary writes $\mathrm{cof}(G) = D F$, and comparison with $\varepsilon D w$ after cancelling $D$ gives $w = \varepsilon F \in V(\lambda)$. Uniqueness gives $\iota(w) = G$, which is claim 5. A lemma on the standard lattice describes $V_0$ and shows that $w$ lies in $V_0$ and is primitive, which is claim 4.

For claim 3, let $\gamma^\ast\gamma = 1$. Then $\det \gamma$ is a unit. Let $g_t$ be the inverse transpose of the image of $\gamma^{-1}$ under $\tau_t$, and put $c(\gamma) = \prod_t \det(g_t)^{s_t}$. A lemma identifies $\bar\gamma^\star$ with the letter action of $g$. The letter action keeps $\mathcal{H}_a$, and claim 3 of the Corollary gives $\mathrm{cof}(g \ast \iota v) = \prod_t \det(g_t)^{-s_t} \varepsilon D (g \cdot v)$. By uniqueness, $\iota(\rho(\gamma) v) = c(\gamma) \cdot g \ast \iota(v)$, since $\rho(\gamma)$ is the action of $g$ on $V(\lambda)$ and the factors $\det(g_t)^{\pm s_t}$ cancel.

For claim 6, let $P \in \mathcal{H}_a^{\mathcal{O}}$ and write $P = \iota(v)$. The frame reading has integer coefficients, so the coefficients of $\mathrm{cof}(P)$ are integral over $\mathbb{Z}$. Hence $D v = \varepsilon\,\mathrm{cof}(P)$ has integral coefficients. A lemma on saturation by determinants says that this forces $v \in V_0$. $\square$

**Remark 2.1.11.** The Theorem is a form of the theorem of Kashiwara and Vergne: the harmonic polynomials of a given type for the pair $(\mathrm{U}(p, q), \mathrm{U}(n))$ form an irreducible module of the compact group, with a highest weight vector given by a product of minors. Here the irreducibility is replaced by the explicit identification with $V(\lambda)$. The lattice $V_0$, the action $\rho$ and the extremal vectors are not unfolded in this section.

**Remark 2.1.12 (Formalization).** The Theorem is [WeightVariableFormula.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/WeightVariableFormula.lean#L1973), with its five steps at L1640 (division by determinants), L894 (image), L1323 (injectivity), L1545 (surjectivity, with the irreducibility lemma at L657) and L922 (equivariance). The map $\varphi$ is used only to get characteristic $0$ and the Fock positivity at L362. The monotony of $a$ is used only in the surjectivity. The Corollary at L2044 only specializes $K$. Its second name [HodgeWeightDominanceCondition.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HodgeWeightDominanceCondition.lean#L52) is proved by a `first` combinator with six branches, and the third name at [HodgeWeightDominanceConditionStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/HodgeWeightDominanceConditionStatement.lean#L7) by another `first`. Its title does not describe the statement. The record is [IsIntegralCoeffCof.lean](lean:Development/AbelianVarietyTheory/Proofs/CuspFormEvaluations/IsIntegralCoeffCof.lean#L82), with the record type at [ThClassPinsRec.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThClassPinsRec.lean#L45) and [ThClass.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThClass.lean#L123). The frame reading and $D$ are at [LetAct.lean](lean:Development/AbelianVarietyTheory/Definitions/ThetaValues/LetAct.lean#L19), the harmonic set at [RowDeg.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/RowDeg.lean#L43) and $\nabla(\nu)$ at [StatementA.lean](lean:Formalism/GradedWeylDivisibility/StatementA.lean#L24).
