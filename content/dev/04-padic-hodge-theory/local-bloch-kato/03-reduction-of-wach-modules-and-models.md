---
title: Reduction of Wach modules and models
decls:
  - GlobalTheory.RedFun.realD
  - GlobalTheory.BasePairs.exists_modTh_of_pres
  - GlobalTheory.BasePairs.real_of_presented
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Reduction of Wach modules and models

The bounds on admissible classes in Sections 4 and 5 are computed on the side of $(\varphi, \Gamma)$-modules over $k((X))$, where $k$ is the residue field of $\mathcal{O}$. This section sets up that side. It defines lattice families in such modules, a *reduction functor* from representations over $k$ to these modules, and a *model theory*, which gives a lattice family to each residual representation that comes from an admissible one. A local situation is *real* when such data exist. The section proves that every local situation is real, under the properties of Wach modules that the admitted inputs supply. The result is used in [the top theorem](/entry/twisted-lattice-cohomology-theorem-top/).

We keep the notation of Section 1. A *local situation* consists of $K$, $L$, $n \ge 1$, $r$, embeddings $\tau_i : K_0 \to L$ for $i \in \mathbb{Z}/n$, top data of rank $r$ and Galois data, such that the standing hypotheses hold, the Galois data are of top type, and T1, T2 and T3 hold. A *residue field* of the situation is a field $k$ of characteristic $\ell$ with a surjective ring map $\mathcal{O} \to k$ whose kernel is $\lambda \mathcal{O}$.

Fix $k$ and a $(\varphi, \gamma)$-ring structure $R = (\varphi, \gamma)$ on $k((X))$, as in Section 2. For a $k[[X]]$-submodule $N$ of a $k((X))$-vector space $V$ and $a \in \mathbb{Z}$ put $X^a N = \{X^a x : x \in N\}$, and for a $k$-linear $f : V \to V$ let $f^* N$ be the $k[[X]]$-span of $f(N)$. $N$ is a *lattice* if it is finitely generated and spans $V$ over $k((X))$.

**Definition 7.3.1 ($(\varphi, \gamma)$-module with letters).** A *$(\varphi, \gamma)$-module with $n$ letters* is a finite-dimensional $k((X))$-vector space $V$ with $k$-linear maps $\varphi_i, \gamma_i : V \to V$ for $i \in \mathbb{Z}/n$ such that $\varphi_i(ax) = \varphi(a)\varphi_i(x)$, the image of $\varphi_i$ spans $V$, $\gamma_i(ax) = \gamma(a)\gamma_i(x)$, $\gamma_i$ is bijective, and $\varphi_i \circ \gamma_{i-1} = \gamma_i \circ \varphi_i$.

A *lattice family* is a family $N = (N_i)_{i \in \mathbb{Z}/n}$ of $k[[X]]$-submodules of $V$. Let $w_i, w_i'$ be integers. The family satisfies *(A, B)* for $(w, w')$ if $\varphi_i^* N_{i-1} \subseteq X^{-w_i} N_i$ and $X^{w_i'} N_i \subseteq \varphi_i^* N_{i-1}$ for all $i$. It satisfies *(C)* if $\gamma_i(x) - x \in X N_i$ for all $x \in N_i$.

Let $\nabla_i = X^{-1}(\gamma_i - 1)$. For $x \in k$ let $E_x$ be the set of $v \in V$ with $(\nabla_i - x)^m v \in X N_i$ for some $m$. The *Sen multiplicity* $\mathrm{sen}_i(N, x)$ is the dimension over $k$ of $(N_i \cap E_x)/(X N_i \cap E_x)$. Under (C), $\nabla_i$ maps $N_i$ and $X N_i$ into themselves, and this is the multiplicity of $x$ as an eigenvalue of $\nabla_i$ on $N_i / X N_i$. For a multiset $U$ of integers and $w \in \mathbb{Z}$ let $\mathrm{rc}(U, w, x)$ be the number of $u \in U$ with $u - w = x$ in $k$. We say that $N$ has an *$E$-polynomial* at $i$ of level $s$ if there is a polynomial $f$ over $k$ with $f(0) \ne 0$ and $\nabla_i f(\nabla_i) x \in X^s N_i$ for all $x \in N_i$.

**Definition 7.3.2 (Reduction functor).** A *reduction functor* $F$ for $R$ with $n$ letters consists of:

1. a class of *objects*, which are representations of $G_K$ on spaces $k^m$, closed under subrepresentations, quotients and sums (if $A \oplus B \to C$ is a surjective map of representations and $A$, $B$ are objects, so is $C$), and containing the trivial character $\mathbf{1}$;
2. for each representation $A$ on $k^m$ a $(\varphi, \gamma)$-module $F(A)$ with $n$ letters on $k((X))^m$;
3. for each $k$-linear $f : A \to B$ and letter $i$ a $k((X))$-linear map $F_i(f)$, such that for $G_K$-maps between objects $F_i(f) \varphi_i = \varphi_i F_{i-1}(f)$, $F_i(f) \gamma_i = \gamma_i F_i(f)$, $F_i$ is additive, $k$-linear and functorial, and $F_i(f)$ is injective or surjective when $f$ is;
4. nonzero vectors $u_i \in F(\mathbf{1})$ with $\varphi_i(u_{i-1}) = u_i$ and $\gamma_i(u_i) = u_i$;
5. for an object $A$ and a family $x_i \in F(A)$ with $\varphi_i(x_{i-1}) = x_i$ and $\gamma_i(x_i) = x_i$, a $G_K$-map $f : \mathbf{1} \to A$ with $F_i(f)(u_i) = x_i$ for all $i$.

For $f : A \to B$, the *push* of a lattice family $N$ of $F(A)$ is $(F_i(f)(N_i))_i$, and the *pullback* of a family $N'$ of $F(B)$ is $(F_i(f)^{-1}(N_i'))_i$.

**Definition 7.3.3 (Model theory).** Fix top data of rank $r$ and a reduction functor $F$. Put $w_i' = h_i - w_i$. A *model theory* consists of:

1. a representation $T$ of $G_K$ on $k^r$ and a character $\omega : G_K \to k^\times$ with $\omega^e \ne 1$ for $0 < e < \ell - 1$;
2. a class of *base pairs* $(A, N)$, with $A$ an object and $N$ a lattice family of lattices in $F(A)$, such that each base pair satisfies (A, B) for $(w, w')$ and (C); for some $\mu$ the representation $A$ has the semisimplification of $\mu$ copies of $T \oplus \bigoplus_{e=0}^{t-1} \omega^{-e}$, and $\mathrm{sen}_i(N, x) = \mu\, \mathrm{rc}(\tilde U_i, w_i, x)$; for two base pairs $(A, N)$ and $(B, N')$ there are $G_K$-maps $a : A \to C$ and $b : B \to C$ with $A \oplus B \to C$ bijective such that $(C, (a_* N)_i + (b_* N')_i)$ is a base pair; and if T1 and T3 hold, each letter $i$ of type Bd has an $E$-polynomial of level $w_i' + 1$;
3. a lattice family $N^{\mathrm{std}}$ of $F(T)$ that is a model of $T$ (see below), with $\mathrm{sen}_i(N^{\mathrm{std}}, x) = \mathrm{rc}(U_i, w_i, x)$;
4. for each integer $e$ with $-1 \le e < t$, the character $\omega^{-e}$ is an object, and a lattice family $N^{e}$ of lattices in $F(\omega^{-e})$ with (C), $\varphi_i^* N^e_{i-1} = X^e N^e_i$, and $\mathrm{sen}_i(N^e, x) = 1$ if $x = e$ in $k$ and $0$ otherwise; $N^e$ is a model of $\omega^{-e}$ for $0 \le e < t$, and $N^0_i = k[[X]] u_i$.

A *model* of a representation $A$ is a lattice family $N$ of $F(A)$ for which there are a base pair $(B, N_b)$, a representation $A_1$, an injective $G_K$-map $j : A_1 \to B$ and a surjective $G_K$-map $p : A_1 \to A$ with $N = p_*(j^* N_b)$.

**Definition 7.3.4 (Real local situation).** A local situation is *real* if for every residue field $k$ there are a $(\varphi, \gamma)$-ring structure $R$ on $k((X))$, a cyclotomic embedding $\iota$ for $R$, a reduction functor $F$ for $R$ with $n$ letters and a model theory $M$, such that:

1. $\omega(g)$ is the image of $\varepsilon(g)$ in $k$ for all $g$;
2. there is a surjective $\mathcal{O}$-linear map $q : T_0 \to k^r$ with kernel $\lambda T_0$ and $q(\chi_1(g)^{-1} g x) = T(g) q(x)$;
3. for every admissible representation $\pi$ on an $\mathcal{O}$-module $N$, every representation $A$ of $G_K$ on $k^m$ and every $\mathcal{O}$-linear bijection $e : N \to k^m$ with $e(\chi_1(g)^{-1} \pi(g) x) = A(g) e(x)$, the representation $A$ has a model.

Now we bring in the Wach data of the period data at $(K, L)$, which exist in Case A. We use these parts: a ring $\Lambda = \prod_{i_0 \in \mathbb{Z}/n_0} \mathcal{O}[[X]]$, with $n_0 = [K_0 : \mathbb{Q}_\ell]$ and idempotents $e_{i_0}$; embeddings $\tau^W_{i_0} : K_0 \to L$; a group $\Gamma$ with an injective character $\chi_\Gamma : \Gamma \to \mathcal{O}^\times$ and a finite subgroup $\Delta \subseteq \Gamma$; an action $\gamma_0$ of $\Gamma$ on $\mathcal{O}[[X]]$ and the element $\pi_{01} = 1 - \ell + \sum_{\delta \in \Delta} \gamma_0(\delta)(1+X)$; for each lattice $T$ a module $D(T)$ over $\Lambda$ with semilinear operators $\varphi_D$ and $\gamma_D(g)$ for $g \in \Gamma$; a *Wach submodule* $N(T) \subseteq D(T)$; and maps $D(f) : D(T') \to D(T)$ for maps of lattices $f : T' \to T$. Let $D^\Delta(T)$ be the elements of $D(T)$ fixed by $\Delta$. A map $q : T \to k^m$ onto a representation $A$ is a *quotient map* if it is $\mathcal{O}$-linear, surjective and $G_K$-equivariant.

**Definition 7.3.5 (Presentation).** Let $F$ be a reduction functor for $R$, $\iota$ cyclotomic for $R$, $\tau : \mathbb{Z}/n \to \mathbb{Z}/n_0$ and $\gamma \in \Gamma$. A *presentation* consists of:

1. the equality $\iota(X) = \overline{\pi_{01}}$, the reduction of $\pi_{01}$ modulo the kernel of $\mathcal{O} \to k$;
2. for each quotient map $q : T \to A$, the representation $A$ is an object;
3. for each quotient map $q : T \to A$ and letter $i$, a surjective additive map $j_i : D^\Delta(T) \to F(A)$ with:
   - $j_i(a x) = c\, j_i(x)$ when $a \in \Lambda$, $c \in k[[X]]$ and $\iota(c) = \overline{a_{\tau(i)}}$;
   - $j_i(\varphi_D x) = \varphi_i(j_{i-1} x)$ and $j_i(\gamma_D(\gamma) x) = \gamma_i(j_i x)$;
   - if $f : T' \to T$ is injective with image $\ker q$, then $j_i(x) = 0$ if and only if $e_{\tau(i)} x = D(f)(y)$ for some $y$;
   - for a second quotient map $q' : T' \to A'$, a map of lattices $f : T \to T'$ and a $G_K$-map $g : A \to A'$ with $q' \circ f = g \circ q$, we have $j_i'(D(f) x) = F_i(g)(j_i x)$;
4. for each quotient map $q$ of the trivial lattice $\mathcal{O}$ onto $\mathbf{1}$ and each $x \in D^\Delta(\mathcal{O})$ that generates $N(\mathcal{O})$ over $\Lambda$, the vectors $j_i(x)$ and $u_i$ span the same $k[[X]]$-line.

A local situation is *presented* if for every residue field $k$ there are $R$, a cyclotomic $\iota$, $F$, $\tau$ and $\gamma$ with $\tau^W_{\tau(i)} = \tau_i$ for all $i$, $\chi_\Gamma(\gamma) = 1 + \ell$, and a presentation.

The Wach data have *the used properties* if six conditions hold. We name them and do not unfold them: a basis of $N(T)$ in $D^\Delta(T)$ for crystalline $T$; bounds for $\varphi_D$ on $N(T)$ by the jumps of $T$; an exact form of these bounds for crystalline characters; saturation of $N(T)$ under maps that are bijective after inverting $\ell$; additivity of $N$ for sums of lattices; and a Sen operator $\nu$ with $\gamma_D(\gamma) y - y = \pi_0 \nu(y)$ on $N(T)^\Delta$, whose characteristic polynomial modulo $\pi_0 + \ell$ is given by the jumps.

**Theorem 7.3.6 (Presentations exist).** Let the period data carry $A_{\inf}$-data, Wach data $H$ and Fontaine data $E$ for $H$. Then every local situation is presented.

Lean: `GlobalTheory.RedFun.realD`.

*Proof.* Let $k$ be a residue field. Since $\ell \ge 5$, there is a $(\varphi, \gamma)$-ring structure $R$ on $k((X))$ with a cyclotomic embedding $\iota$, and $\iota(X)$ is determined. The reduction of the $\Gamma$-action gives $\gamma \in \Gamma$ with $\chi_\Gamma(\gamma) = 1 + \ell$. The letter bijection gives $\tau$ with $\tau^W_{\tau(i)} = \tau_i$. A lifting statement for vectors fixed by $\Delta$ and $\gamma$ is also used. The Fontaine data embed each $D(T)$ into $T \otimes R_W$ for a period ring $R_W$, compatibly with $\varphi$ and $G_K$. The reduction functor $F$ and the presentation are built from the reduction modulo $\lambda$ of this embedding by a tensor product construction, which we do not unfold. $\square$

**Theorem 7.3.7 (A model theory from a presentation).** Let $S$ be a local situation and $k$ a residue field, with $R$, cyclotomic $\iota$, $F$, $\tau$ and $\gamma$ as in the definition of presented, and a presentation. Assume that the Wach data have the used properties, and that the crystalline calculus holds: sums and twists of crystalline lattices are crystalline with the expected jumps, $\varepsilon$ is crystalline with jump $-1$, and continuous characters trivial on $I_K$ are crystalline with jump $0$. Then there is a model theory $M$ for $F$ with properties 1, 2 and 3 of the definition of real.

Lean: `GlobalTheory.BasePairs.exists_modTh_of_pres`.

*Proof.* Twist by $\chi_1^{-1}$, which is crystalline with jumps $-w_i$. For a quotient map $q : T \to A$ with kernel $\lambda T$ from a crystalline lattice with jumps $U_i'$, call a lattice family $N$ of $F(A)$ a *reduction* if $N_i = j_i(D^\Delta(T) \cap N(T))$. The base pairs are the reductions of the twists of lattices in sums of $\mu$ full representations. The presentation and the used properties give six facts on reductions: they exist and consist of lattices; they satisfy (A, B) for $(a, b)$ when $a_i, b_i \ge 0$ and $-a_i \le u \le b_i$ for all $u \in U_i'$; $\mathrm{sen}_i(N, x) = \mathrm{rc}(U_i', 0, x)$; they have an $E$-polynomial of level $s \ge 0$ at $i$ when every integer $a$ with $0 \le a < s$ that is congruent modulo $\ell$ to some $u \in U_i'$ is equal to $u$; if $A$ has dimension 1 and $U_i' = \{a_i\}$, then $\varphi_i^* N_{i-1} = X^{a_i} N_i$; and the reduction of a sum is the sum of the reductions. A general construction from these six facts, the standing hypotheses and the crystalline calculus gives the model theory. For $\omega$ we take the reduction of $\varepsilon$, and $\omega^e \ne 1$ for $0 < e < \ell - 1$ holds since $K$ is unramified. $\square$

**Theorem 7.3.8 (Reality from presentations).** Let the period data carry $A_{\inf}$-data, Wach data $H$ and Fontaine data for $H$. Let $S$ be a presented local situation, assume that the Wach data have the used properties and that the crystalline calculus holds. Then $S$ is real.

Lean: `GlobalTheory.BasePairs.real_of_presented`.

*Proof.* This is [Theorem 7.3.7](/entry/exists-mod-th-of-pres/) applied to the data of each residue field that presentedness gives. $\square$

**Remark 7.3.9 (Formalization).** The Fontaine data are a hypothesis of the reality theorem but are not used in its proof. The used properties of Wach modules are one of the admitted inputs of the series. In the top theorem they are taken for the Wach data at each $(K, L)$ in Case A.
