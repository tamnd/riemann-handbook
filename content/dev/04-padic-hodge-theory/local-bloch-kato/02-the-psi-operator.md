---
title: The operator psi
decls:
  - GlobalTheory.PsiShiftProof.lemmaPsi
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The operator $\psi$

The bound on admissible classes in Section 4 works with étale $(\varphi, \Gamma)$-modules over a field of Laurent series in characteristic $\ell$. On such a module the Frobenius has a left inverse $\Psi$, and the key fact is that $\gamma - 1$ maps the kernel of $\Psi$ in one step of a lattice filtration onto the kernel in the next step. This section constructs $\psi$ on the ring and $\Psi$ on the modules and proves these facts. The result is used in [the residual bound](/entry/res-bound-dsum/).

Let $k$ be a field of characteristic $\ell$ and $k((X))$ the field of Laurent series, with the subring $k[[X]]$. For $a \in \mathbb{Z}$ put $D_a = X^a k[[X]]$. Let $\varphi_\pi$ be the $k$-algebra map of $k((X))$ with $\varphi_\pi(X) = X^\ell$, so $\varphi_\pi(\sum c_m X^m) = \sum c_m X^{\ell m}$.

**Definition 7.2.1 (Assembly map).** The *assembly map* $k((X))^\ell \to k((X))$ is
$$(y_0, \dots, y_{\ell-1}) \longmapsto \sum_{j=0}^{\ell-1} (1+X)^j \, \varphi_\pi(y_j).$$

Since $(1+X)^\ell = 1 + X^\ell$ in characteristic $\ell$, the elements $(1+X)^j$ with $0 \le j < \ell$ are a basis of $k((X))$ over the subfield $\varphi_\pi(k((X))) = k((X^\ell))$. So the assembly map is a bijection. The *standard* $\psi_\pi$ sends $x$ to the component $y_0$ of its preimage. It is $k$-linear, and $\psi_\pi(\varphi_\pi(a)x) = a\,\psi_\pi(x)$.

**Definition 7.2.2 (Frobenius and $\Gamma$ on Laurent series).** A *$(\varphi, \gamma)$-ring structure* on $k((X))$ consists of two $k$-algebra maps $\varphi, \gamma : k((X)) \to k((X))$ that commute, both map $k[[X]]$ into $k[[X]]$, $\varphi(X) = u X^\ell$ for a unit $u$ of $k[[X]]$, and $\gamma(X) = X(1 - \kappa X)$ for some $\kappa \in k[[X]]$ with constant term 1.

For $z \in \mathbb{Z}_\ell$ let $\delta_z$ be the substitution $X \mapsto (1+X)^z - 1$ on $k[[X]]$, with the binomial series reduced modulo $\ell$, and let $\gamma_\pi$ be the substitution $X \mapsto (1+X)^{1+\ell} - 1$.

**Definition 7.2.3 (Cyclotomic embedding).** Let $R = (\varphi, \gamma)$ be a $(\varphi,\gamma)$-ring structure on $k((X))$. A $k$-algebra map $\iota : k((X)) \to k((X))$ is *cyclotomic* for $R$ if:

1. $\iota(X) = v X^{\ell - 1}$ for a unit $v$ of $k[[X]]$, and $\iota$ maps $k[[X]]$ into $k[[X]]$;
2. an element $b \in k[[X]]$ is fixed by all $\delta_z$ with $z^{\ell - 1} = 1$ if and only if $b = \iota(a)$ for some $a \in k[[X]]$;
3. $\iota \circ \varphi = \varphi_\pi \circ \iota$;
4. $\iota(\gamma(a)) = \gamma_\pi(\iota(a))$ for $a \in k[[X]]$.

So $\iota$ identifies the ring of $R$ with the subring of the standard ring that is fixed by the group $\Delta$ of the $(\ell-1)$-st roots of unity in $\mathbb{Z}_\ell^\times$. On this subring the standard operators restrict to the operators of $R$.

A $k$-linear map $f$ between $k((X))$-modules is *$\sigma$-semilinear* for a ring map $\sigma$ if $f(ax) = \sigma(a) f(x)$. A *lattice* in a finite-dimensional $k((X))$-vector space $V$ is a finitely generated $k[[X]]$-submodule $M$ that spans $V$. Put $X^a M = \{X^a x : x \in M\}$, and for a $k$-linear $f : V \to V$ let $f^* M$ be the $k[[X]]$-span of $f(M)$.

**Theorem 7.2.4 (The operator $\psi$).** Let $\ell \ge 5$, let $k$ be a field of characteristic $\ell$, let $R = (\varphi, \gamma)$ be a $(\varphi,\gamma)$-ring structure on $k((X))$, and let $\iota$ be cyclotomic for $R$. Then the assembly map is bijective, and there is a $k$-linear map $\psi : k((X)) \to k((X))$ with these properties.

1. If $\iota(x) = \sum_j (1+X)^j \varphi_\pi(y_j)$, then $\iota(\psi(x)) = y_0$.
2. $\psi(\varphi(a)x) = a\,\psi(x)$, $\psi(\varphi(a)) = a$, and $\psi \circ \gamma = \gamma \circ \psi$.
3. For each integer $a$ with $2 - \ell \le a \le 1$, $\psi(D_a) = D_0$.
4. Let $V$ be a finite-dimensional $k((X))$-vector space, $f : V \to V$ a $\varphi$-semilinear map whose image spans $V$, and $g_0, g : V \to V$ two $\gamma$-semilinear maps with $f \circ g_0 = g \circ f$. Then there is a $k$-linear $\Psi : V \to V$ such that
   - (a) $\Psi(a f(x)) = \psi(a) x$ for $a \in k((X))$ and $x \in V$;
   - (b) $\Psi \circ g = g_0 \circ \Psi$;
   - (c) for each lattice $M_0$ in $V$ and each $a$ with $2 - \ell \le a \le 1$, $\Psi(X^a f^* M_0) = M_0$;
   - (d) for each lattice $M_0$ with $g_0(x) - x \in X M_0$ for all $x \in M_0$, and each $a$ with $2 - \ell \le a \le 0$, the map $x \mapsto g(x) - x$ sends $\{x \in X^a f^* M_0 : \Psi(x) = 0\}$ onto $\{x \in X^{a+1} f^* M_0 : \Psi(x) = 0\}$.

Lean: `GlobalTheory.PsiShiftProof.lemmaPsi`.

*Proof.* The assembly map is bijective because $(1+X)^j$, $0 \le j < \ell$, is a basis of $k((X))$ over $k((X^\ell))$.

*Construction of $\psi$.* From conditions 1 and 2, the image of $\iota$ is the set of elements of $k((X))$ fixed by all $\delta_z$ with $z^{\ell-1} = 1$. Each such $\delta_z$ commutes with $\psi_\pi$. So $\psi_\pi$ maps the image of $\iota$ into itself. Since $\iota$ is injective, there is a unique $\psi(x)$ with $\iota(\psi(x)) = \psi_\pi(\iota(x))$, and $\psi$ is $k$-linear. Property 1 is the definition of $\psi_\pi$.

*Property 2.* Apply $\iota$: by condition 3, $\iota(\varphi(a)x) = \varphi_\pi(\iota a)\iota(x)$, and $\psi_\pi(\varphi_\pi(b) y) = b \psi_\pi(y)$. Injectivity of $\iota$ gives the first identity, and the second is the case $x = 1$, since $\psi_\pi(1) = 1$. The standard $\gamma_\pi$ commutes with $\psi_\pi$, and condition 4 gives the third identity.

*Property 3.* Condition 1 gives $\iota(D_a) \subseteq D_{(\ell - 1)a}$, and conversely $\iota(x) \in D_s$ with $s > (\ell-1)(a-1)$ implies $x \in D_a$. The standard $\psi_\pi$ maps $D_s$ into $D_t$ when $\ell t \le s$. For $a \ge 2 - \ell$ we get $\psi(D_a) \subseteq D_0$. In particular $\psi(X) \in k[[X]]$. Its constant term is not zero. Otherwise $\psi(X) \in D_1$, so $\psi_\pi(\iota(X)) = \iota(\psi(X))$ has constant term 0. For $y \in D_{\ell - 1}$ the constant term of $\psi_\pi(y)$ is a nonzero integer multiple of the coefficient of $X^{\ell - 1}$ in $y$. So $\iota(X) \in D_\ell$, hence $X \in D_2$, which is false. So $d\,\psi(X) = 1$ for some $d \in k[[X]]$. For $b \in k[[X]]$ the element $x = \varphi(bd) X$ lies in $D_1 \subseteq D_a$, and $\psi(x) = bd\,\psi(X) = b$. So $\psi(D_a) = D_0$.

*Construction of $\Psi$.* Choose a basis $(b_i)$ of $V$. Since $f$ is semilinear and its image spans $V$, the vectors $c_i = f(b_i)$ span $V$, so they form a basis. Put $\Psi(\sum_i a_i c_i) = \sum_i \psi(a_i) b_i$. Then (a) follows from $\psi(\varphi(a)x) = a\psi(x)$. For (b) it is enough to check $\Psi(g(a c_i)) = g_0(\Psi(a c_i))$. Here $g(a c_i) = \gamma(a) g(f(b_i)) = \gamma(a) f(g_0(b_i))$, so (a) gives $\Psi(g(a c_i)) = \psi(\gamma(a)) g_0(b_i) = \gamma(\psi(a)) g_0(b_i) = g_0(\psi(a) b_i)$.

*Properties (c) and (d).* Choose the basis $(b_i)$ to be a $k[[X]]$-basis of $M_0$. Then $f^* M_0$ is the $k[[X]]$-span of the $c_i$, an element is in $X^s f^* M_0$ when all its coordinates in the basis $(c_i)$ are in $D_s$, and $\Psi(x) = 0$ when $\psi$ kills all coordinates of $x$. So (c) follows from property 3. For (d), let $G$ be the matrix of $g_0$ in the basis $(b_i)$. The hypothesis on $g_0$ says that $G - 1$ has entries in $D_1$. In the basis $(c_i)$ the map $g - 1$ is
$$x \longmapsto \Big( \sum_m \varphi(G_{im})\, \gamma(x_m) - x_i \Big)_i .$$
Apply $\iota$. The matrix $\iota(G) - 1$ has entries in $D_2$, since $\ell - 1 \ge 2$. On the standard side, write each coordinate with $\psi_\pi = 0$ through the assembly map, with $y_0 = 0$. A computation in these components shows that for a matrix $H$ with $H - 1$ in $D_2$ and $\ell \ge 5$, the map $x \mapsto (\sum_m \varphi_\pi(H_{im}) \gamma_\pi(x_m) - x_i)_i$ sends the vectors with $\psi_\pi(x_i) = 0$ and $x_i \in D_{\ell s}$ into the vectors with the same property for $D_{\ell(s+1)}$, onto them, and injectively. The condition $\psi(x) = 0$ and the bounds $2 - \ell \le a \le 0$ let us pass between $D_a$ on the side of $R$ and $D_{\ell a}$ on the standard side. For surjectivity, the preimage that the standard side gives is fixed by $\Delta$: its image under $\delta_z - 1$ is again a solution of the homogeneous equation with $\psi_\pi = 0$, so it is 0 by injectivity. By condition 2 it comes from the side of $R$. $\square$

**Remark 7.2.5 (Formalization).** The assembly map is stated with $\varphi_\pi$ and not with $\varphi$. Property 4 is stated for one triple $(f, g_0, g)$. Its use on a module with operators $\varphi_i, \gamma_i$ indexed by $\mathbb{Z}/n$ takes $f = \varphi_i$, $g_0 = \gamma_{i-1}$ and $g = \gamma_i$.
